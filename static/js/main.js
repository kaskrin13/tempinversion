/* Updating clock code */
tday = new Array("Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday");
tmonth = new Array("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December");

function GetClock() {
    var d = new Date();
    var nday = d.getDay(),
        nmonth = d.getMonth(),
        ndate = d.getDate(),
        nyear = d.getYear();
    if (nyear < 1000) nyear += 1900;
    var nhour = d.getHours(),
        nmin = d.getMinutes(),
        nsec = d.getSeconds(),
        ap;

    if (nhour == 0) {
        ap = " AM";
        nhour = 12;
    } else if (nhour < 12) {
        ap = " AM";
    } else if (nhour == 12) {
        ap = " PM";
    } else if (nhour > 12) {
        ap = " PM";
        nhour -= 12;
    }

    if (nmin <= 9) nmin = "0" + nmin;
    if (nsec <= 9) nsec = "0" + nsec;

    document.getElementById('clockbox').innerHTML = "" + tday[nday] + ", " + tmonth[nmonth] + " " + ndate + ", " + nyear + " " + nhour + ":" + nmin + ":" + nsec + ap + "";
}

window.onload = function() {
    GetClock();
    setInterval(GetClock, 1000);
}

function initMap() {
    /* For new stations add a new var here */
    var station1 = {
        info: '<strong>Aberdeen VTcr, MS</strong>\
                    <br>VT2018-0001<br>',
        lat: 33.723746,  
        long: -88.65824
    };

    var station2 = {
        info: '<strong>Bee Lake, MS</strong>\
                    <br>DREC-2010<br>',
        lat: 33.0443,  
        long: -90.36007
    };

    var station3 = {
        info: '<strong>Brooksville, MS</strong>\
                    <br>DREC-2006<br>',
        lat: 33.2599,  
        long: -88.56284
    };

    var station4 = {
        info: '<strong>Brooksville2 VTso, MS</strong>\
                    <br>VT2018-0002<br>',
        lat: 33.239933,  
        long: -88.5129
    };

    var station5 = {
        info: '<strong>Brown Loam Exp Stn VT, MS</strong>\
                    <br>VT2018-0003<br>',
        lat: 32.21274,  
        long: -90.52107
    };

    var station6 = {
        info: '<strong>Brown Loam Exp. Stn, MS</strong>\
                    <br>DREC-2019<br>',
        lat: 32.21022,  
        long: -90.51228
    };

    var station7 = {
        info: '<strong>Catladge Farm, MS</strong>\
                    <br>DS-0003<br>',
        lat: 32.666566,  
        long: -90.968841
    };

    var station8 = {
        info: '<strong>Clarksdale VTso, MS</strong>\
                    <br>VT2018-0006<br>',
        lat: 34.059234,  
        long: -90.577096
    };

    var station9 = {
        info: '<strong>Cleveland, MS</strong>\
                    <br>DS-0002<br>',
        lat: 33.758496,  
        long: -90.815173
    };

    var station10 = {
        info: '<strong>COOP Stoneville, MS</strong>\
                    <br>COOP-Stoneville<br>',
        lat: 33.431177,  
        long: -90.910764
    };
    
    var station11 = {
        info: '<strong>Cypress Farm, MS</strong>\
                    <br>DS-0001<br>',
        lat: 34.073390,  
        long: -90.482674
    };

    var station12 = {
        info: '<strong>Jackson Co, MS</strong>\
                    <br>DREC-2011<br>',
        lat: 30.6392,  
        long: -88.46277
    };

    var station13 = {
        info: '<strong>Longwood VTso, MS</strong>\
                    <br>VT2018-0007<br>',
        lat: 33.301961,  
        long: -91.005963
    };
    
    var station14 = {
        info: '<strong>Lyon, MS</strong>\
                    <br>DREC-2001<br>',
        lat: 34.24959,  
        long: -90.54206
    };

    var station15 = {
        info: '<strong>Macon VTcr, MS</strong>\
                    <br>VT2019-0008<br>',
        lat: 33.1469,  
        long: -88.51698
    };
    
    var station16 = {
        info: '<strong>Mound Bayou, MS</strong>\
                    <br>DREC-2013<br>',
        lat: 33.87123,  
        long: -90.70963
    };

    var station17 = {
        info: '<strong>Olive Branch VTcr, MS</strong>\
                    <br>VT2018-0005<br>',
        lat: 34.89863,  
        long: -89.899648
    };

    var station18 = {
        info: '<strong>Olive Branch2 VTso, MS</strong>\
                    <br>VT2018-0009<br>',
        lat: 34.867305,  
        long: -89.976208
    };

    var station19 = {
        info: '<strong>Onward VT, MS</strong>\
                    <br>VT2018-0010<br>',
        lat: 32.76372,  
        long: -91.075301
    };

    var station20 = {
        info: '<strong>Pontotoc AWS COOP, MS</strong>\
                    <br>COOP-0002<br>',
        lat: 34.138698,  
        long: -89.006969
    };
    
    var station21 = {
        info: '<strong>Prairie, MS</strong>\
                    <br>DREC-2007<br>',
        lat: 33.79764,  
        long: -88.65915
    };
    
    var station22 = {
        info: '<strong>Sidon, MS</strong>\
                    <br>DREC-2003<br>',
        lat: 33.42334,  
        long: -90.2346
    };
    
    var station23 = {
        info: '<strong>Stockett Farm, MS</strong>\
                    <br>DREC-2012<br>',
        lat: 31.04377,  
        long: -91.31052
    };
    
    var station24 = {
        info: '<strong>Stoneville AWS, MS</strong>\
                    <br>DREC-2004<br>',
        lat: 33.43122,  
        long: -90.91077
    };
    
    var station25 = {
        info: '<strong>Stoneville F10, MS</strong>\
                    <br>DREC-2015<br>',
        lat: 33.416512,  
        long: -90.913961
    };

    var station26 = {
        info: '<strong>Stoneville SW, MS</strong>\
                    <br>DREC-2009<br>',
        lat: 33.40542,  
        long: -90.92729
    };
    
    var station27 = {
        info: '<strong>Stoneville W, MS</strong>\
                    <br>DREC-2014<br>',
        lat: 33.42269,  
        long: -90.957882
    };
    
    var station28 = {
        info: '<strong>Thighman, MS</strong>\
                    <br>DREC-2002<br>',
        lat: 33.35738,  
        long: -90.50306
    };

    var station29 = {
        info: '<strong>Tippo VT, MS</strong>\
                    <br>VT2018-0012<br>',
        lat: 33.95679,  
        long: -90.1657
    };

    var station30 = {
        info: '<strong>Tribbett, MS</strong>\
                    <br>DREC-2008<br>',
        lat: 33.35236,  
        long: -90.80201
    };
    
    var station31 = {
        info: '<strong>Verona, MS</strong>\
                    <br>DREC-2005<br>',
        lat: 34.16466,  
        long: -88.72394
    };

    var station32 = {
        info: '<strong>Verona VTso, MS</strong>\
                    <br>VT2018-0004<br>',
        lat: 34.166325,  
        long: -88.734339
    };

    /* and here */
    var locations = [
        [station1.info, station1.lat, station1.long, 0],
        [station2.info, station2.lat, station2.long, 1],
        [station3.info, station3.lat, station3.long, 2],
        [station4.info, station4.lat, station4.long, 3],
        [station5.info, station5.lat, station5.long, 4],
        [station6.info, station6.lat, station6.long, 5],
        [station7.info, station7.lat, station7.long, 6],
        [station8.info, station8.lat, station8.long, 7],
        [station9.info, station9.lat, station9.long, 8],
        [station10.info, station10.lat, station10.long, 9],
        [station11.info, station11.lat, station11.long, 10],
        [station12.info, station12.lat, station12.long, 11],
        [station13.info, station13.lat, station13.long, 12],
        [station14.info, station14.lat, station14.long, 13],
        [station15.info, station15.lat, station15.long, 14],
        [station16.info, station16.lat, station16.long, 15],
        [station17.info, station17.lat, station17.long, 16],
        [station18.info, station18.lat, station18.long, 17],
        [station19.info, station19.lat, station19.long, 18],
        [station20.info, station20.lat, station20.long, 19],
        [station21.info, station21.lat, station21.long, 20],
        [station22.info, station22.lat, station22.long, 21],
        [station23.info, station23.lat, station23.long, 22],
        [station24.info, station24.lat, station24.long, 23],
        [station25.info, station25.lat, station25.long, 24],
        [station26.info, station26.lat, station26.long, 25],
        [station27.info, station27.lat, station27.long, 26],
        [station28.info, station28.lat, station28.long, 27],
        [station29.info, station29.lat, station29.long, 28],
        [station30.info, station30.lat, station30.long, 29],
        [station31.info, station31.lat, station31.long, 30],
        [station32.info, station32.lat, station32.long, 31]
    ];

    var map = new google.maps.Map(document.getElementById('map'), {
        zoom: 6,
        center: new google.maps.LatLng(31.284673, -89.556397),
        mapTypeId: google.maps.MapTypeId.TERRAIN
    });

    var infowindow = new google.maps.InfoWindow({});

    var marker, i;

    for (i = 0; i < locations.length; i++) {
        marker = new google.maps.Marker({
            position: new google.maps.LatLng(locations[i][1], locations[i][2]),
            map: map
        });

        google.maps.event.addListener(marker, 'click', (function(marker, i) {
            return function() {
                infowindow.setContent(locations[i][0]);
                infowindow.open(map, marker);
            }
        })(marker, i));

        /* This displays the infowindow for the last item in locations */
        infowindow.setContent(locations[i][0]);
        infowindow.open(map, marker);
    }
}

$(document).ready(function() {
    setTimeout(function(){
        $('body').addClass('loaded');
    }, 10000); /* Loading time, currently 10s */
});
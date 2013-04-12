/*
 * Licensed to the Apache Software Foundation (ASF) under one
 * or more contributor license agreements.  See the NOTICE file
 * distributed with this work for additional information
 * regarding copyright ownership.  The ASF licenses this file
 * to you under the Apache License, Version 2.0 (the
 * "License"); you may not use this file except in compliance
 * with the License.  You may obtain a copy of the License at
 *
 * http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing,
 * software distributed under the License is distributed on an
 * "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
 * KIND, either express or implied.  See the License for the
 * specific language governing permissions and limitations
 * under the License.
 */

var image_id;
var app = {
    // Application Constructor
    initialize: function() {
                    console.log("initialize()");
                    console.log("initajax...");
                    initAjax();
                    console.log("bindecents...");
                    this.bindEvents();
                    console.log("allowcrossdomainpages...");
                    $.mobile.allowCrossDomainPages = true;
                    console.log("hooking click...");
                    $('#photo-btn').click(function(e) {
                        e.preventDefault();
                        console.log("takephoto");
                        takePhoto();
                    });
                    console.log("hooking click publish...");
                    $('#publish-image').bind('click', function(e) {
                        e.preventDefault();
                        console.log("publishing");
                        publishImage();
                    })
                },
    // Bind Event Listeners
    //
    // Bind any events that are required on startup. Common events are:
    // 'load', 'deviceready', 'offline', and 'online'.
    bindEvents: function() {
                    console.log("bindevents...");
                    document.addEventListener('deviceready', this.onDeviceReady, false);
                },
    // deviceready Event Handler
    //
    // The scope of 'this' is the event. In order to call the 'receivedEvent'
    // function, we must explicity call 'app.receivedEvent(...);'
    onDeviceReady: function() {
                    console.log("ondeviceready");
                       app.receivedEvent('deviceready');
                   },
    // Update DOM on a Received Event
    receivedEvent: function(id) {
                   }
};

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function initAjax() {
    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
                xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
        }
    });
}


function takePhoto() {
    navigator.camera.getPicture(getPic,
            null,
            {
                quality:49,
        destinationType:0,
        allowEdit : true
            });
};

function getPic(data) {
    //her ligger bildeinfoen
    var imageTaken = document.getElementById('pictureTaken');
    imageTaken.style.display='block';
    imageTaken.style.width="100%";
    imageTaken.src = "data:image/jpeg;base64,"+data; //her legger vi bildet ut som b64, mens "data" er selve strengen

    sendImage(data);
}

function sendImage(data) {
    alert("attempting to send data beginning with " + data.slice(0,10,0));
    console.log("attempting to send image encoded as base64");
    data.length && $.ajax({ 
        type: "POST", 
        url: "/upload/post", 
        data: {
            "base64_image": document.getElementById('pictureTaken').src
        },
        success: function(data) {
            image_id = data['image_id'];
            alert(image_id);
        },
        error: function() {
            alert("massive failure");
        }
    })
}

function  publishImage(image_id) {
    console.log("attempting to publish image" + image_id);
    image_id && $.ajax({ 
        type: "POST", 
        url: "/upload/publish", 
        data: {
            "image_id":image_id
        },
        success: function(data) {
            alert("published image"); 
        },
        error: function() {
            alert("massive failure");
        }
    })
    window.location = "/";
}

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
                    initAjax();
                    this.bindEvents();
                    $.mobile.allowCrossDomainPages = true;
                    $('#photo-btn').click(function(e) {
                        e.preventDefault();
                        takePhoto();
                    });
                    $('#publish-image').bind('click', function(e) {
                        e.preventDefault();
                        publishImage();
                    })
                },
    //
    // Bind Event Listeners
    //
    // Bind any events that are required on startup. Common events are:
    // 'load', 'deviceready', 'offline', and 'online'.
    bindEvents: function() {
                    document.addEventListener('deviceready', this.onDeviceReady, false);
                },
    // deviceready Event Handler
    //
    // The scope of 'this' is the event. In order to call the 'receivedEvent'
    // function, we must explicity call 'app.receivedEvent(...);'
    onDeviceReady: function() {
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
            function failure(message){
                console.log("error");
                console.log(message);
            },
            {
                quality : 75, 
                destinationType : Camera.DestinationType.DATA_URL, 
                sourceType : Camera.PictureSourceType.CAMERA, 
                allowEdit : true,
                encodingType: Camera.EncodingType.JPEG,
                targetWidth: 1024,
                targetHeight: 1024
            });
};

function getPic(data) {
    sendImage(data);
}

function sendImage(data) {
    data.length && $.ajax({ 
        type: "POST", 
        url: "/upload/post/", 
        data: {
            "base64_image": data
        },
        success: function(data) {
            image_id = data['image_id'];
        },
        error: function() {
        }
    })
}

function  publishImage(image_id) {
    image_id && $.ajax({ 
        type: "POST", 
        url: "/upload/publish", 
        data: {
            "image_id":image_id
        },
        success: function(data) {
        },
        error: function() {
        }
    })
    window.location = "/";
}

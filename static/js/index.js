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

var app = {
    // Application Constructor
    initialize: function() {
                    this.bindEvents();
                    $.mobile.allowCrossDomainPages = true;
                    $('#photo-btn').click(function(e) {
                        takePhoto();
                    });
                    $('#publish-image').bind('click', function(e) {
                        alert("yolo");
                    })
                },
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

$.ajaxSetup({
    beforeSend: function(xhr, settings) {
            xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
    }
});

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

function sendImage(base64_image) {
    $.ajax({ 
        type: "POST", 
        url: "/upload/post", 
        data: {
            "base64_image":base64_image
        } 
    })
}

function  publishImage(image_id) {
    $.ajax({ 
        type: "POST", 
        url: "/upload/publish", 
        data: {
            "image_id":image_id
        }
    })
}
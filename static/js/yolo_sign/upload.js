/**
 * Created by kunkun on 14-3-19.
 */

function upload(p_url) {
    var form = new FormData();
    var fileInput = document.getElementById("inputFile");
    var modelType = document.getElementById("modelType").value;
    form.append("file", fileInput.files[0]);
    form.append("type", modelType);
    $.ajax({
        url: p_url,
        type: 'POST',
        data: form,
        async: false,
        cache: false,
        contentType: false,
        processData: false,
        success: function (result) {
            //var result = JSON.parse(result)
            console.log("result");
            console.log(result);
            if (result.status == 0) {
                alert("detect over!!!");
                fillResponse(result.pub_name);
            } else {
                alert(JSON.stringify(result));
            }
        },
        error: function (result) {
            alert(JSON.stringify(result));
        }
    });
}

function detectUrl(p_url) {
    var form = new FormData();
    var url = document.getElementById("imageUrl").value;
    var modelType = document.getElementById("modelType").value;
    form.append("url", url);
    form.append("type", modelType);
    $.ajax({
        url: p_url,
        type: 'POST',
        data: form,
        async: false,
        cache: false,
        contentType: false,
        processData: false,
        success: function (result) {
            //var result = JSON.parse(result)
            console.log("result");
            console.log(result);
            if (result.status == 0) {
                alert("detect over!!!");
                fillResponse(result.pub_name);
            } else {
                alert(JSON.stringify(result));
            }
        },
        error: function (result) {
            alert(JSON.stringify(result));
        }
    });
}

function fillResponse(pub_name) {
    document.getElementById('myImage').src = '/static/uploads/' + pub_name + '?t=' + new Date().getTime()
}

window.onload = function () {
    var fileInput = document.getElementById("inputFile");
    var img = document.getElementById("myImage");
    var uploadButton = document.getElementById("uploadButton");
    uploadButton.addEventListener("click", function () {
        upload(post_url);
    });

    var detectUrlButton = document.getElementById("detectUrlButton");
    detectUrlButton.addEventListener("click", function () {
        detectUrl(post_detect_url);
    });

    fileInput.addEventListener('change', function () {
        var file = this.files[0];
        var reader = new FileReader();
        reader.readAsDataURL(file);
        reader.onload = function (e) {
            img.src = this.result;
        }
    }, false);
}


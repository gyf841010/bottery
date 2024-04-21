/**
 * Created by flynt on 24-04-21.
 */

function get_code(g_url) {
    $.ajax({
        url: g_url,
        type: "get",
        success: function (data) {
            alert(JSON.stringify(data));
            fillResponse(data)
        },
        error: function () {
            alert("错误");
        }
    });
}

function fillResponse(pub_name) {
    // TODO 把结果写入页面
}

window.onload = function () {
    get_code(get_url);
}


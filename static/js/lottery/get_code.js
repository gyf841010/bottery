/**
 * Created by flynt on 24-04-21.
 */

function get_code(g_url) {
    //alert(g_url);
    $.ajax({
        url: g_url,
        type: "get",
        success: function (data) {
            fillResponse(JSON.parse(data))
        },
        error: function () {
            alert("错误");
        }
    });
}

function fillResponse(data) {
    // TODO 把结果写入页面
    document.getElementById('myDate').textContent = "开奖日期：" + data['date']
    document.getElementById('n1').textContent = data['lottery'][0]
    document.getElementById('n2').textContent = data['lottery'][1]
    document.getElementById('n3').textContent = data['lottery'][2]
    document.getElementById('n4').textContent = data['lottery'][3]
    document.getElementById('n5').textContent = data['lottery'][4]
    document.getElementById('n6').textContent = data['lottery'][5]
}

window.onload = function () {
    get_code(get_url);
}


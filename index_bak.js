

var authorization;
var phone = ""; // 需要输入的用户手机号

fetch('/Users/golfy/Documents/睡眠文档/sleepReport/Sleepreport_liu/王尔卓.txt')
.then(res => res.text())
.then(con => {
  processData(con);
})
.catch(err => console.error(err));

function processData(con) {

  const lines = con.split('\n');
  lines.forEach((e, idx) => {
    console.log(`Processing line ${idx}: ${e}`);
  });
}

$.getJSON("result_sleep.json", function (result) {

  phone = result["phone"];
  $.ajaxSetup({
    beforeSend: function (xhr) {
      if (authorization != null) {
        xhr.setRequestHeader('Authorization', authorization)
      }
    }
  })
  $.get("https://miniprogram.semacare.cn/api/wx/user/login-phone?phone=" + phone + "&code=998080", function (data, status) {
    if (status == "success") {
      authorization = data["data"];
      $.get("https://miniprogram.semacare.cn/api/member/get-current-user-member-info", function (data, status) {
        if (status == "success") {
          $("#idname").text(data["data"]["name"]);
          $("#idgender").text(data["data"]["gender"] == 1 ? "男" : "女");
          $("#idage").text(birthday2age(data["data"]["birthdate"])+"岁");
          var height = data["data"]["height"];
          var weight = data["data"]["weight"];
          $("#idheight").text(height + "cm");
          $("#idweight").text(weight + "kg");
          var h = Number("1.57");
          var w = Number("60");
          $("#idbmi").text(Math.round(w / (h * h) * 10) / 10); // 这样做是为了保留小数点后一位
        }
      });
    }
  })

  var deep_sleep_total_count = Number(result["deep_sleep_total_count"]);
  var deep_sleep_count_arr = result["deep_sleep_count_arr"];
  var light_sleep_total_count = Number(result["light_sleep_total_count"]);
  var light_sleep_count_arr = result["light_sleep_count_arr"];
  var rem_sleep_total_count = Number(result["rem_sleep_total_count"]);
  var rem_sleep_count_arr = result["rem_sleep_count_arr"];
  var other_sleep_total_count = Number(result["other_sleep_total_count"]);
  var other_sleep_count_arr = result["other_sleep_count_arr"];
  var wake_sleep_total_count = Number(result["wake_sleep_total_count"]);
  var wake_sleep_count_arr = result["wake_sleep_count_arr"];

  var sleep_time_arr = result["sleep_time_arr"];
  var sleep_value_arr = result["sleep_value_arr"];

  var start_time = sleep_time_arr[0];
  start_time = start_time.substring(0, start_time.length-3);
  var start_timestamp = Date.parse(start_time)/1000; // 毫秒

  var end_time = sleep_time_arr[sleep_time_arr.length-1];
  end_time = end_time.substring(0, end_time.length-3);
  var end_timestamp = Date.parse(end_time)/1000; // 毫秒

  var sleep_time = end_timestamp - start_timestamp + 60;
  var sleep_time_str = Math.floor(sleep_time / 3600) + "小时" + Math.ceil(sleep_time / 60 % 60) + "分钟";

  $("#sleep_time").text(sleep_time_str);
  $("#sleep_time_range").text(start_time + " ~ " + end_time);

  var wake_time_str = Math.floor(wake_sleep_total_count / 60) + "小时" + Math.ceil(wake_sleep_total_count % 60) + "分钟";
  $("#wake_sleep_time").text(wake_time_str);
  var rem_sleep_time_str = Math.floor(rem_sleep_total_count / 60) + "小时" + Math.ceil(rem_sleep_total_count % 60) + "分钟";
  $("#rem_sleep_time").text(rem_sleep_time_str);
  var light_sleep_time_str = Math.floor(light_sleep_total_count / 60) + "小时" + Math.ceil(light_sleep_total_count % 60) + "分钟";
  $("#light_sleep_time").text(light_sleep_time_str);
  var deep_sleep_time_str = Math.floor(deep_sleep_total_count / 60) + "小时" + Math.ceil(deep_sleep_total_count % 60) + "分钟";
  $("#deep_sleep_time").text(deep_sleep_time_str);
  var other_sleep_time_str = Math.floor(other_sleep_total_count / 60) + "小时" + Math.ceil(other_sleep_total_count % 60) + "分钟";
  $("#other_sleep_time").text(other_sleep_time_str);

  var rem_sleep_time_scale = Math.ceil(rem_sleep_total_count * 60 / sleep_time * 100);
  var light_sleep_time_scale = Math.ceil(light_sleep_total_count * 60 / sleep_time * 100);
  var deep_sleep_time_scale = Math.ceil(deep_sleep_total_count * 60 / sleep_time * 100);
  var other_sleep_time_scale = Math.ceil(other_sleep_total_count * 60 / sleep_time * 100);
  $("#wake_sleep_time_scale").text(100 - rem_sleep_time_scale - light_sleep_time_scale - deep_sleep_time_scale - other_sleep_time_scale);
  $("#rem_sleep_time_scale").text(rem_sleep_time_scale);
  $("#light_sleep_time_scale").text(light_sleep_time_scale);
  $("#deep_sleep_time_scale").text(deep_sleep_time_scale);
  $("#other_sleep_time_scale").text(other_sleep_time_scale);



  $("#mean_hr").text(result["mean_hr"] + " bpm");
  $("#max_hr").text(result["max_hr"] + " bpm");
  $("#min_hr").text(result["min_hr"] + " bpm");

  var hr_value_arr = result["hr_value_arr"];

  var tmp_hr_time_arr = [];
  for (let i = 0; i < sleep_time_arr.length; i++) {
    var tmp_hr_time = sleep_time_arr[i];
    tmp_hr_time_arr.push(tmp_hr_time.substring(11, 16));
  }

  hrOption = {
    grid: {
      left: 30,
      right: 10,
      top: 10,
      bottom: 30,
    },
    xAxis: {
      type: 'category',
      data: tmp_hr_time_arr
    },
    yAxis: {
      type: 'value'
    },
    series: [
      {
        data: hr_value_arr,
        type: 'line'
      }
    ]
  };

  if (hrOption && typeof hrOption === 'object') {
    hrMyChart.setOption(hrOption);
  }

  let deep_sleep_color = 'green';
  let light_sleep_color = 'yellow';
  let rem_sleep_color = 'red';
  let other_sleep_color = 'blue';
  let wake_sleep_color = 'silver';

  var data = [];
  var deep_sleep_data = [];
  var light_sleep_data = [];
  var rem_sleep_data = [];
  var other_sleep_data = [];
  var wake_sleep_data = [];
  for (let i = 0; i < sleep_value_arr.length; i++) {
    var data_style = {};
    var data_style_color = {};


    let value = sleep_value_arr[i];
    var color;
    data_style["value"] = "3";
    if (value == "1") {
      color = deep_sleep_color;
      deep_sleep_data.push("2");
      light_sleep_data.push("-");
      rem_sleep_data.push("-");
      other_sleep_data.push("-");
      wake_sleep_data.push("-");
    } else if (value == "2") {
      color = light_sleep_color;
      deep_sleep_data.push("-");
      light_sleep_data.push("2");
      rem_sleep_data.push("-");
      other_sleep_data.push("-");
      wake_sleep_data.push("-");
    } else if (value == "3") {
      color = rem_sleep_color;
      deep_sleep_data.push("-");
      light_sleep_data.push("-");
      rem_sleep_data.push("2");
      other_sleep_data.push("-");
      wake_sleep_data.push("-");
    } else if (value == "4") {
      color = other_sleep_color;
      deep_sleep_data.push("-");
      light_sleep_data.push("-");
      rem_sleep_data.push("-");
      other_sleep_data.push("2");
      wake_sleep_data.push("-");
    } else if (value == "0") {
      color = wake_sleep_color;
      deep_sleep_data.push("-");
      light_sleep_data.push("-");
      rem_sleep_data.push("-");
      other_sleep_data.push("-");
      wake_sleep_data.push("2");
    }
    data_style_color["color"] = color;
    data_style["itemStyle"] = data_style_color;

    data.push(data_style);
  }

  sleepOption = {
    legend: {
      data: ["熟睡","浅睡","REM","清醒","其他"],
      left: 'left'
    },
    grid: {
      left: 15,
      right: 10,
      top: 40,
      bottom: 30,
    },
    xAxis: {
      type: 'category',
      data: tmp_hr_time_arr,
    },
    yAxis: {
      show: false,
      type: 'value'
    },
    series: [
      {
        name: "熟睡",
        data: deep_sleep_data,
        type: 'bar',
        barWidth: '100%',
        stack: 'Total',
        itemStyle: {
          color: deep_sleep_color,
        },
      },
      {
        name: "浅睡",
        data: light_sleep_data,
        type: 'bar',
        barWidth: '100%',
        stack: 'Total',
        itemStyle: {
          color: light_sleep_color,
        },
      },
      {
        name: "REM",
        data: rem_sleep_data,
        type: 'bar',
        barWidth: '100%',
        stack: 'Total',
        itemStyle: {
          color: rem_sleep_color,
        },
      },
      {
        name: "清醒",
        data: wake_sleep_data,
        type: 'bar',
        barWidth: '100%',
        stack: 'Total',
        itemStyle: {
          color: wake_sleep_color,
        },
      },
      {
        name: "其他",
        data: other_sleep_data,
        type: 'bar',
        barWidth: '100%',
        stack: 'Total',
        itemStyle: {
          color: other_sleep_color,
        },
      },
    ]
  };


  if (sleepOption && typeof sleepOption === 'object') {
    sleepMyChart.setOption(sleepOption);
  }

});



var sleepDom = document.getElementById('chart-container');
var sleepMyChart = echarts.init(sleepDom, null, {
  renderer: 'canvas',
  useDirtyRect: false
});
var sleepApp = {};
var sleepOption;

window.addEventListener('resize', sleepMyChart.resize);

var hrDom = document.getElementById('chart-container3');
var hrMyChart = echarts.init(hrDom, null, {
  renderer: 'canvas',
  useDirtyRect: false
});
var hrApp = {};
var hrOption;

window.addEventListener('resize', hrMyChart.resize);


function birthday2age(strAge) {
  const birArr = strAge.split("-");
  const birYear = Number(birArr[0]);
  const birMonth = Number(birArr[1]);
  const birDay = Number(birArr[2]);

  const today = new Date();
  const nowYear = today.getFullYear();
  const nowMonth = today.getMonth() + 1; //记得加1
  const nowDay = today.getDate();
  let returnAge;

  if (birArr === null) {
    return false
  };
  const d = new Date(birYear, birMonth - 1, birDay);

  if (d.getFullYear() === birYear && (d.getMonth() + 1) === birMonth && d.getDate() === birDay) {
    if (nowYear === birYear) {
      returnAge = 0; // 
    } else {
      let ageDiff = nowYear - birYear; // 
      if (ageDiff > 0) {
        if (nowMonth === birMonth) {
          let dayDiff = nowDay - birDay; // 
          if (dayDiff < 0) {
            returnAge = ageDiff - 1;
          } else {
            returnAge = ageDiff;
          }
        } else {
          let monthDiff = nowMonth - birMonth; // 
          if (monthDiff < 0) {
            returnAge = ageDiff - 1;
          } else {
            returnAge = ageDiff;
          }
        }
      } else {
        return 0; //返回-1 表示出生日期输入错误 晚于今天
      }
    }
    return returnAge;
  } else {
    return 0;
  }
} 
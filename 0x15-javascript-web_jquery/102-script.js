$(document).ready(() => {
  $("#btn_translate").click(() => {
    const url = "https://www.fourtonfish.com/hellosalut/hello/";
    const lang = $("#language_code").val();
    $.getJSON(url + lang, (data) => {
      $("#hello").text(data.hello);
    });
  });
});

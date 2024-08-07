$(document).ready(function(){
  function fetchTranslation() {
    var langCode = $('#language_code').val();
    var apiUrl = 'https://www.fourtonfish.com/hellosalut/hello/?lang=' + langCode;
    
    $.get(apiUrl, function(data) {
      $('#hello').text(data.hello);
    });
  }

  $('#btn_translate').click(fetchTranslation);

  $('#language_code').keypress(function(event) {
    if (event.which == 13) { // Enter key pressed
      fetchTranslation();
    }
  });
});

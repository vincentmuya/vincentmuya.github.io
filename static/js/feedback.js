$(document).ready(function(){
  $('form').submit(function(event){
    event.preventDefault()
    form = $("form")

    $.ajax({
      'url':'/ajax/feedback/',
      'type':'POST',
      'data':form.serialize(),
      'dataType':'json',
      'success': function(data){
        alert(data['success'])
      },
    })// END of Ajax method
    $('#id_question_Feedback').val('')
    $("#id_email").val('')
  }) // End of submit event

}) // End of document ready function

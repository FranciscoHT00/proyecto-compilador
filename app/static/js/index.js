$(document).ready(function () {
  $("#run_btn").prop("disabled", true);

  $("#validate_btn").on("click", validateCode);
  $("#run_btn").on("click", runCode);
});

function validateCode() {
  var code = $("#code_input").val();
  code += "\n";

  console.log(code);

  $.ajax({
    data: {
      code: code,
    },
    type: "POST",
    dataType: "json",
    url: "/run",
  })
    .done(function (response) {
      $("#console").val(response);
    })
    .fail(function (jqXHR, textStatus, errorThrown) {
      alert(errorThrown);
    });
}

function runCode() {}

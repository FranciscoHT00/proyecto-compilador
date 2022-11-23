$(document).ready(function () {
  $("#run_btn").on("click", runCode);

  $("#example_btn").on("click", loadExample);
});

function runCode() {
  var code = $("#code_input").val();
  code += "\n";

  console.log(code);

  playMessage("Codice in esecuzione.");

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

function loadExample() {
  var option = $("#examples").val();

  var example = "";

  if (option === "example_1") {
    example += `
    5  REM HELLO WORLD PROGAM
    10 IMPRIMICION "HELLO WORLD"
    99 KO`;
  } else {
    if (option === "example_2") {
      example += `
      10 DEF FDX(X) = 2*X
      20 DESDE I = 0 HASTA 100
      30 IMPRIMICION FDX(I)
      40 PROXIMARDO I
      50 KO`;
    } else {
      example += `
      5 IMPRIMICION "THIS PROGRAM COMPUTES AND PRINTS THE NTH POWERS"
      6 IMPRIMICION "OF THE NUMBERS LESS THAN OR EQUAL HASTA N DESDE VARIOUS"
      7 IMPRIMICION "N FROM 1 THROUGH 7"
      8 IMPRIMICION
      10 DESDE N = 1 HASTA 7
      15 IMPRIMICION "N = "N
      20 DESDE I = 1 HASTA N
      30 IMPRIMICION I^N,
      40 PROXIMARDO I
      50 IMPRIMICION
      60 IMPRIMICION
      70 PROXIMARDO N
      80 KO`;
    }
  }

  $("#code_input").val(example);
  playMessage("Esempio caricato.");
}

function playMessage(text) {
  var message = new SpeechSynthesisUtterance();
  message.volume = 1;
  message.rate = 1;
  message.pitch = 1;
  message.text = text;
  message.lang = "it-IT";

  speechSynthesis.speak(message);
}

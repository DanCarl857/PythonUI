// TODO: Modularize code and write utility functions
  function getAllCheckBoxes(){

    var acceptedVals = [];

    $("input[name='accepted_values']:checked").each(function(){
      acceptedVals.push($(this).val());
    });

    var accepted_vals = JSON.stringify(acceptedVals);

    $.ajax({
      url: 'http://localhost:8000/accept?vals=' + accepted_vals + '&id=1',
      data: accepted_vals,
      dataType: 'json',
      success: function(data){
      }
    });

    console.log("In this function now man");
    setTimeout(function(){
      location.reload();
    }, 10000);
    
  }

  // PLEASE IGNORE REDUNDANCY.... :-)
  function getRejectedBoxes() {

     var rejectedVals = [];

     $("input[name='accepted_values']:checked").each(function(){
      rejectedVals.push($(this).val());
     });

     var rejected_vals = JSON.stringify(rejectedVals);

     $.ajax({
      url: 'http://localhost:8000/reject?vals=' + rejected_vals + '&id=2',
      data: rejected_vals,
      dataType: 'json',
      success: function(data){

      }
     });
  }

  function undoAccept(){

    var checkVals = [];

    $("input[name='acc_values']").each(function(){
      checkVals.push($(this).val());
    });


    var check_vals = JSON.stringify(checkVals);
    console.log(check_vals);

    $.ajax({
      url: 'http://localhost:8000/undo?vals=' + check_vals,
      data: check_vals,
      dataType: 'json',
      success: function(data){

      }
    });
  }

  function undoRej(){

    var cheVals = [];

    $("input[name='rej_values']").each(function(){
      cheVals.push($(this).val());
    });

    var rejected_vals = JSON.stringify(cheVals);

    $.ajax({
      url: 'http://localhost:8000/undo?vals=' + rejected_vals,
      data: rejected_vals,
      dataType: 'json',
      success: function(data){

      }
    });
  }

  function commitChanges(){
    $('#commitModal').modal({
      backdrop: 'static',
      keyboard: false
    });

    setTimeout(function(){
      $('#committing').fadeIn();
    }, 3000);

    setTimeout(function(){
      $('#don').fadeIn();
    }, 5000);

    setTimeout(function(){
      $('#commitModal').modal('hide');
    }, 8000);
  }

  function discardChanges(){
    $('#discardModal').modal({
      backdrop: 'static',
      keyboard: false
    });

    undoAccept();

    setTimeout(function(){
      $('#discarding').fadeIn();
    }, 3000);

    undoRej();

    setTimeout(function(){
      $('#done').fadeIn();
    }, 5000);

    setTimeout(function(){
      $('#discardModal').modal('hide');
    }, 8000);

    setTimeout(function(){
      location.reload();
    }, 10000);
  }

  function ignoreAll(){

  }

/*
  $("#empresa").on("keyup", function() {
    var value = $(this).val();

    $("table tr").each(function(index) {
        if (index != 0) {

            $row = $(this);

            var id = $row.find("td:first").text();

            if (id.indexOf(value) != 0) {
                $(this).hide();
            }
            else {
                $(this).show();
            }
        }
    });
});​
*/
  

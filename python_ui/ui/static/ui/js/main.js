// TODO: Modularize code and write utility functions
  function getAllCheckBoxes(){

    var acceptedVals = [];

    $("input[name='accepted_values']:checked").each(function(){
      acceptedVals.push($(this).val());
    });

    var accepted_vals = JSON.stringify(acceptedVals);

    $('#genericModal').modal({
      backdrop: 'static',
      keyboard: false
    });

    $.ajax({
      url: 'http://localhost:8000/accept?vals=' + accepted_vals + '&id=1',
      data: accepted_vals,
      dataType: 'html',
      method:'get',
      success: function(data){
        $('#genericModal').modal('hide');
        location.reload();
      }
    });
  }

  // PLEASE IGNORE REDUNDANCY.... :-)
  function getRejectedBoxes() {
      $('#genericModal').modal({
        backdrop: 'static',
        keyboard: false
      });


     var rejectedVals = [];

     $("input[name='accepted_values']:checked").each(function(){
      rejectedVals.push($(this).val());
     });

     var rejected_vals = JSON.stringify(rejectedVals);

     $.ajax({
      url: 'http://localhost:8000/reject?vals=' + rejected_vals + '&id=2',
      data: rejected_vals,
      dataType: 'html',
      method: 'get',
      success: function(data){
        $('#genericModal').modal('hide');
        location.reload();
      }
     });
  }

  function undoAccept(){
    $('#genericModal').modal({
        backdrop: 'static',
        keyboard: false
    });

    var checkVals = [];

    $("input[name='acc_values']").each(function(){
      checkVals.push($(this).val());
    });


    var check_vals = JSON.stringify(checkVals);
    console.log(check_vals);

    $.ajax({
      url: 'http://localhost:8000/undo?vals=' + check_vals,
      data: check_vals,
      dataType: 'html',
      method: 'get',
      success: function(data){
        $('#genericModal').modal('hide');
        location.reload();
      }
    });
  }

  function undoRej(){
    $('#genericModal').modal({
        backdrop: 'static',
        keyboard: false
    });

    var cheVals = [];

    $("input[name='rej_values']").each(function(){
      cheVals.push($(this).val());
    });

    var rejected_vals = JSON.stringify(cheVals);

    $.ajax({
      url: 'http://localhost:8000/undo?vals=' + rejected_vals,
      data: rejected_vals,
      dataType: 'html',
      success: function(data){
        $('#genericModal').modal('hide');
        location.reload();
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
     $('#deleteModal').modal('hide');
     $('#genericModal').modal({
        backdrop: 'static',
        keyboard: false
      });
    var ignoreVals = [];

     $("input[name='accepted_values']:checked").each(function(){
      ignoreVals.push($(this).val());
     });

     var ignore_vals = JSON.stringify(ignoreVals);

     $.ajax({
      url: 'http://localhost:8000/delete?vals=' + ignore_vals,
      data: ignore_vals,
      dataType: 'html',
      method: 'get',
      success: function(data){
        $('#genericModal').modal('hide');
        location.reload();
      }
     });

  }

  function confirmReq(){
    $('#deleteModal').modal({
        backdrop: 'static',
        keyboard: false
    });
  }

  function reloadPage(){
    $('#deleteModal').modal('hide');
    location.reload();
  }


function filterTable(tclass, that){
  console.log(that.value);
  $("table tr ."+ tclass).each(function(){
    var text = $(this).text();
    if(text.toLowerCase().indexOf(that.value.toLowerCase())<0 ){
      $(this).parent('tr').hide();
    }else{
      $(this).parent('tr').show();
    }
  });
}
  

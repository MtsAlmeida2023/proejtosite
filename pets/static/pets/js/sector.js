function countResidents(checkedSector, residents){

    var totalLabel = document.getElementById('totalChecked');
    var previousValue = parseInt(totalLabel.innerText);
    var newValue = residents;
    
    if (!checkedSector.checked){
        newValue = newValue * (-1);
    }
    
    var newTotal = previousValue + newValue;
    
    totalLabel.innerText = newTotal.toString();

    //console.log(newTotal);
    // totalChecked.value = newTotal;





}


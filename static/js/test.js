async function postData(data1, data2){

    if (data1.length < 1 || data2.length < 1) return
        
    let formData = new FormData();
    formData.append('data1', data1);
    formData.append('data2', data2);

    const request = await fetch("https://100075.pythonanywhere.com/dowell_training_webapi/dowelltraining2web/", { 
        
      method: 'POST',
      body: formData,

    });
    
    const response = await request.text();

    console.log(response);

}




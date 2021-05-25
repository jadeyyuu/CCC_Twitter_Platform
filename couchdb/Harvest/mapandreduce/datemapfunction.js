function(doc) { if(doc.date && doc.text) 
    { var created = new Date(doc.date);
        emit([created.getFullYear(),created.getMonth()+1,created.getDate()],doc.text); }}

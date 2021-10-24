var page = 0

function paginate(route){
    $('.load-more img').attr('src', '/static/images/loading.gif')
    page += 1
    $.get(`/dashboard/${route}/paginate/${page}`, function(data, status){
        appendItem(data.items, route)
    })
}

function appendItem(items, route){
    var html = ''
    
    if(items){
        alert(items)
    }
    
    $('.paginate img').attr('src', '/images/load-more.png')
    $('.item-wrapper').append(html)

}
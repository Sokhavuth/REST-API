//asset/js/index.js

function next(){
  
  $('.loading').html("<img src='/static/images/loading.gif' />")

  $.get(`/random`, 
    
    function(data, status){
      if(status === 'success'){
        genVideo(data)
      }
  })
}

function home(){
  
  $('.loading').html("<img src='/static/images/loading.gif' />")
  $.get(`/random`, 
    
    function(data, status){
      if(status === 'success'){
        genVideo(data)
      }
  })
}

function previous(){
  
  $('.loading').html("<img src='/static/images/loading.gif' />")
  $.get(`/random`, 
    
    function(data, status){
      if(status === 'success'){
        genVideo(data)
      }
  })
}

function genVideo(data){
  var html = ''
  
  for(var v=0; v< data.videos.length; v++){
    html += `<div class='wrapper'>`
    html += `<a class='thumb' href='/video/${ data["videos"][v][0] }'>`
    html += `<img src="${ data['videos'][v][4] }" />`
    html += `</a>`
    html += `<a href='/video/${ data["videos"][v][0] }'>`
    html += `<img class='play-icon' src='/static/images/play.png' />`
    if(v === 0){
      html += `<div class='loading'></div>`
    }
    html += `</a>`
    html += `<a class='post-title' href='/video/${ data["videos"][v][0] }'>`
    html += `${data['videos'][v][1]}`
    html += `</a>`
    //html += `<span class='date' id='date${ v }'></span>`
    //html += `<script>`
    //html += `$('#date${ v }').html(new Date("${ data['videos'][v][6] }").toLocaleDateString())`
    //html += `</script>`
    html += `</div>`
  }
  $('.loading').empty()
  $('.front_widget').html(html)

}

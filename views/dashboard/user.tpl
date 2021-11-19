<!--views/dashboard/user.tpl-->
<link rel='stylesheet' href='/static/styles/post.css' />
<script src="/static/scripts/ckeditor/ckeditor.js"></script>
<script src="/static/scripts/video.js"></script>

<section class='Main'>
    <div class='content'>
        <form action='/dashboard/post' method='post' >
            %if 'edit' in data:
            
            %else:
            <input type='text' name='title' placeholder='ឈ្មោះ' required />
            <textarea name="content" id="editor" ></textarea>
            <div class='wrapper'>
                <select name='category'>
                    <option>អ្នក​និពន្ធ</option>
                    <option>អ្នក​គ្រប់គ្រង</option>
                </select>
                <input type='text' name='thumb' required placeholder="តំណរ​ភ្ជាប់​រូប​តំណាង" />
                <input type='datetime-local' value='' name='datetime' required />
                <input type='submit' value='ចុះ​ផ្សាយ' />
            </div>
            <input name='entries' value='' type='hidden' />
            %end
        </form>

        <div class='form'>
            <select name='type'>
                <option>YouTube</option>
                <option>YouTubePlaylist</option>
                <option>Facebook</option>
                <option>OK</option>
                <option>Dailymotion</option>
                <option>Vimeo</option>
            </select>
            <input name='id' type='text' placeholder="អត្តសញ្ញាណវីដេអូ" required />
            <select name='ending'>
                <option>ចប់​ហើយ</option>
                <option>មិន​ទាន់ចប់</option>
            </select>
            <input onclick='genJson()' type="button" value="បញ្ចូល​វីដេអូ" />
        </div>

        <table class='viddata'></table>
        
        %if 'edit' in data:
            <script>
                var entries = JSON.parse('{{!data["item"][6]}}')
            </script>
        %end

        <script>
        if(entries.length > 0){

            let html = ``
            for(let v in entries){
                episode += 1
                html += `<tr>`
                html += `<td title="Delete" onClick="deleteRow(event)" class="episode">${episode}</td>`
                html += `<td class="td${episode}">${entries[v].type}</td>`
                html += `<td class="td${episode}">${entries[v].id}</td>`
                html += `<td class="td${episode}">${entries[v].ending}</td>`
                html += `</tr>`
            }

            if($('.viddata').html() === ''){
                $('.viddata').append('<tr>')
                $('.viddata').append('<th>ភាគ/លុប</th>')
                $('.viddata').append('<th>ប្រភេទ​</th>')
                $('.viddata').append('<th>អត្តសញ្ញាណ​</th>')
                $('.viddata').append('<th>ចប់ឬ​នៅ?</th>')
                $('.viddata').append('</tr>')
            }

            $('.viddata').append(`${html}`)

        }
        </script>

        <script src="/static/scripts/ckeditor/config.js"></script>
    </div>
</section>
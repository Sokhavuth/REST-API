<!--views/dashboard/post.tpl-->
<link rel='stylesheet' href='/static/styles/post.css' />
<script src="/static/scripts/ckeditor/ckeditor.js"></script>
<script src="/static/scripts/video.js"></script>

<section class='Main'>
    <div class='content'>
        <form action='/dashboard/post' method='post' >
            <input type='text' name='title' placeholder='ចំណងជើង' required />
            <textarea name="content" id="editor" ></textarea>
            <div class='wrapper'>
                <select name='category' >
                    %for category in data['categories']:
                        <option>{{ category[0] }}</option>
                    %end
                </select>
                <input type='text' name='thumb' required placeholder="តំណរ​ភ្ជាប់​រូប​តំណាង" />
                <input type='datetime-local' value='' name='datetime' required />
                <input type='submit' value='ចុះ​ផ្សាយ' />
            </div>
            <input name='entries' value='' type='hidden' />
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
    
        <script src="/static/scripts/ckeditor/config.js"></script>
    </div>
</section>


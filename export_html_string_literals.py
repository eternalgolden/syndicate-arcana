'''
    export_html_string_literals.py

    contains the string literals necessary for html

'''

# div starter -> div_profile_NAME -> div_text_starter -> text -> div_ender

DIV_STARTER = "<div class=\"newline-container\"> \
        <div class=\"profpiccontainer\">"

DIV_PROFILE_GEB =  "<div class=\"profpic-GEB\"> \
                <img src=\"https://cdn.discordapp.com/emojis/1257910386355867720.jpg\"></img> \
            </div> \
            <p>G.E.B</p></div>"

DIV_PROFILE_YISANG =  "<div class=\"profpic-YISANG\"> \
                <img src=\"https://cdn.discordapp.com/emojis/1257920236943048806.jpg\"></img> \
            </div> \
            <p>이 상</p></div>"


DIV_PROFILE_YIGEUM =  "<div class=\"profpic-YIGEUM\"> \
                <img src=\"https://cdn.discordapp.com/emojis/1257920172828790856.jpg\"></img> \
            </div> \
            <p>이 금</p></div>"

DIV_PROFILE_BETH =  "<div class=\"profpic-BETH\"> \
                <img src=\"https://cdn.discordapp.com/emojis/1257920160782745600.jpg\"></img> \
            </div> \
            <p>베스</p></div>"

DIV_PROFILE_LUDMILA =  "<div class=\"profpic-LUDMILA\"> \
                <img src=\"https://cdn.discordapp.com/emojis/1257920168735019038.jpg\"></img> \
            </div> \
            <p>류드밀라</p></div>"

DIV_PROFILE_MONTAG =  "<div class=\"profpic-MONTAG\"> \
                <img src=\"https://cdn.discordapp.com/emojis/1257920171394469958.jpg\"></img> \
            </div> \
            <p>몬태그</p></div>"


DIV_PROFILE_MING =  "<div class=\"profpic-MING\"> \
                <img src=\"https://cdn.discordapp.com/emojis/1257920169788047515.jpg\"></img> \
            </div> \
            <p>밍기뉴</p></div>"

DIV_PROFILE_HEATH =  "<div class=\"profpic-HEATH\"> \
                <img src=\"https://cdn.discordapp.com/emojis/1257920165656662016.jpg\"></img> \
            </div> \
            <p>히스클리프</p></div>"

DIV_PROFILE_FLEUR =  "<div class=\"profpic-FLEUR\"> \
                <img src=\"https://cdn.discordapp.com/emojis/1266809603321233498.jpg\"></img> \
            </div> \
            <p>플뢰르</p></div>"

DIV_PROFILE_GAHWAN =  "<div class=\"profpic-GAHWAN\"> \
                <img src=\"https://cdn.discordapp.com/emojis/1257920163827810378.jpg\"></img> \
            </div> \
            <p>가환</p></div>"

DIV_PROFILE_HONGLU =  "<div class=\"profpic-HONGLU\"> \
                <img src=\"https://cdn.discordapp.com/emojis/1257920167220875304.jpg\"></img> \
            </div> \
            <p>홍루</p></div>"

DIV_PROFILE_ANON =  "<div class=\"profpic-ANON\"> \
                <img src=\"https://cdn.discordapp.com/emojis/1267226470044930223.jpg\"></img> \
            </div> \
            <p>그림자</p></div>"

DIV_PROFILE_HERMIT =  "<div class=\"profpic-HERMIT\"> \
                <img src=\"https://cdn.discordapp.com/emojis/1267226513464627332.jpg\"></img> \
            </div> \
            <p>은둔자</p></div>"

DIV_TEXT_STARTER = "<div class=\"text\">"

DIV_ENDER = "</div> \
    </div>"

DIV_FINISHED = " \
</body> \
</html> \
"
DIV_HEADER = " \
<!DOCTYPE html> \
<html> \
<head> \
    <style> \
        .newline-container {width: 100%; height: fit-content; background-color: #3c3c3c; display: flex; flex-direction: row; border-bottom: 2px solid black;} \
        .newline-container .text {width: 70%; height: fit-content; margin: 30px; color: white;} \
        .newline-container .profpiccontainer {margin: 10px; margin-top: 20px; margin-left: 20px; width: 10%; height: fit-content; align-items: center;} \
        \
        .newline-container .profpiccontainer .profpic-GEB {padding-top:100%; height: 0; overflow: hidden; box-sizing: border-box; position: relative; border-radius: 10px; border: 5px solid #ffa000; min-width: 60px;} \
        .newline-container .profpic-GEB img {width: 100%; vertical-align: top; position: absolute; top: 0; left: 0; height: 100%; object-fit: cover;} \
        .newline-container .profpiccontainer .profpic-GEB p {min-width: 60px; width: 100%; text-align: center; color:#FFA000;} \
        \
        .newline-container .profpiccontainer .profpic-YISANG {padding-top:100%; height: 0; overflow: hidden; box-sizing: border-box; position: relative; border-radius: 10px; border: 5px solid #ffa000; min-width: 60px;} \
        .newline-container .profpic-YISANG img {width: 100%; vertical-align: top; position: absolute; top: 0; left: 0; height: 100%; object-fit: cover;} \
        .newline-container .profpiccontainer .profpic-YISANG p {min-width: 60px; width: 100%; text-align: center; color:#FFA000;} \
        \
        .newline-container .profpiccontainer .profpic-YIGEUM {padding-top:100%; height: 0; overflow: hidden; box-sizing: border-box; position: relative; border-radius: 10px; border: 5px solid #ffa000; min-width: 60px;} \
        .newline-container .profpic-YIGEUM img {width: 100%; vertical-align: top; position: absolute; top: 0; left: 0; height: 100%; object-fit: cover;} \
        .newline-container .profpiccontainer .profpic-YIGEUM p {min-width: 60px; width: 100%; text-align: center; color:#FFA000;} \
        \
        .newline-container .profpiccontainer .profpic-BETH {padding-top:100%; height: 0; overflow: hidden; box-sizing: border-box; position: relative; border-radius: 10px; border: 5px solid #ffa000; min-width: 60px;} \
        .newline-container .profpic-BETH img {width: 100%; vertical-align: top; position: absolute; top: 0; left: 0; height: 100%; object-fit: cover;} \
        .newline-container .profpiccontainer .profpic-BETH p {min-width: 60px; width: 100%; text-align: center; color:#FFA000;} \
        \
        .newline-container .profpiccontainer .profpic-LUDMILA {padding-top:100%; height: 0; overflow: hidden; box-sizing: border-box; position: relative; border-radius: 10px; border: 5px solid #ffa000; min-width: 60px;} \
        .newline-container .profpic-LUDMILA img {width: 100%; vertical-align: top; position: absolute; top: 0; left: 0; height: 100%; object-fit: cover;} \
        .newline-container .profpiccontainer .profpic-LUDMILA p {min-width: 60px; width: 100%; text-align: center; color:#FFA000;} \
        \
        .newline-container .profpiccontainer .profpic-MONTAG {padding-top:100%; height: 0; overflow: hidden; box-sizing: border-box; position: relative; border-radius: 10px; border: 5px solid #ffa000; min-width: 60px;} \
        .newline-container .profpic-MONTAG img {width: 100%; vertical-align: top; position: absolute; top: 0; left: 0; height: 100%; object-fit: cover;} \
        .newline-container .profpiccontainer .profpic-MONTAG p {min-width: 60px; width: 100%; text-align: center; color:#FFA000;} \
        \
        .newline-container .profpiccontainer .profpic-MING {padding-top:100%; height: 0; overflow: hidden; box-sizing: border-box; position: relative; border-radius: 10px; border: 5px solid #ffa000; min-width: 60px;} \
        .newline-container .profpic-MING img {width: 100%; vertical-align: top; position: absolute; top: 0; left: 0; height: 100%; object-fit: cover;} \
        .newline-container .profpiccontainer .profpic-MING p {min-width: 60px; width: 100%; text-align: center; color:#FFA000;} \
        \
        .newline-container .profpiccontainer .profpic-HEATH {padding-top:100%; height: 0; overflow: hidden; box-sizing: border-box; position: relative; border-radius: 10px; border: 5px solid #ffa000; min-width: 60px;} \
        .newline-container .profpic-HEATH img {width: 100%; vertical-align: top; position: absolute; top: 0; left: 0; height: 100%; object-fit: cover;} \
        .newline-container .profpiccontainer .profpic-HEATH p {min-width: 60px; width: 100%; text-align: center; color:#FFA000;} \
        \
        .newline-container .profpiccontainer .profpic-FLEUR {padding-top:100%; height: 0; overflow: hidden; box-sizing: border-box; position: relative; border-radius: 10px; border: 5px solid #FFF8E7; min-width: 60px;} \
        .newline-container .profpic-FLEUR img {width: 100%; vertical-align: top; position: absolute; top: 0; left: 0; height: 100%; object-fit: cover;} \
        .newline-container .profpiccontainer .profpic-FLEUR p {min-width: 60px; width: 100%; text-align: center; color:#FFF8E7;} \
        \
        .newline-container .profpiccontainer .profpic-GAHWAN {padding-top:100%; height: 0; overflow: hidden; box-sizing: border-box; position: relative; border-radius: 10px; border: 5px solid #8A0707; min-width: 60px;} \
        .newline-container .profpic-GAHWAN img {width: 100%; vertical-align: top; position: absolute; top: 0; left: 0; height: 100%; object-fit: cover;} \
        .newline-container .profpiccontainer .profpic-GAHWAN p {min-width: 60px; width: 100%; text-align: center; color:#8A0707;} \
        \
        .newline-container .profpiccontainer .profpic-HONGLU {padding-top:100%; height: 0; overflow: hidden; box-sizing: border-box; position: relative; border-radius: 10px; border: 5px solid #9CD5C2; min-width: 60px;} \
        .newline-container .profpic-HONGLU img {width: 100%; vertical-align: top; position: absolute; top: 0; left: 0; height: 100%; object-fit: cover;} \
        .newline-container .profpiccontainer .profpic-HONGLU p {min-width: 60px; width: 100%; text-align: center; color:#9CD5C2;} \
        \
        .newline-container .profpiccontainer .profpic-ANON {padding-top:100%; height: 0; overflow: hidden; box-sizing: border-box; position: relative; border-radius: 10px; border: 5px solid #ffa000; min-width: 60px;} \
        .newline-container .profpic-ANON img {width: 100%; vertical-align: top; position: absolute; top: 0; left: 0; height: 100%; object-fit: cover;} \
        .newline-container .profpiccontainer .profpic-ANON p {min-width: 60px; width: 100%; text-align: center; color:#FFF8E7;} \
        \
        .newline-container .profpiccontainer .profpic-HERMIT {padding-top:100%; height: 0; overflow: hidden; box-sizing: border-box; position: relative; border-radius: 10px; border: 5px solid #ffa000; min-width: 60px;} \
        .newline-container .profpic-HERMIT img {width: 100%; vertical-align: top; position: absolute; top: 0; left: 0; height: 100%; object-fit: cover;} \
        .newline-container .profpiccontainer .profpic-HERMIT p {min-width: 60px; width: 100%; text-align: center; color:#FFF8E7;} \
        \
    </style>\
</head>\
\
<body>\
"

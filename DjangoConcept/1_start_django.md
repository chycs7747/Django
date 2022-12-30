request message

Request head: request line + header lines
Request line: method + url + version
entity body: 사용자가 요청을 서버에 보낼 때 쓰는 부분



response message
status line: version + status code + phrase

* 이 status code에 404error 같은게 들어간다.
* phrase에는 간단하게 성공실패여부가 들어감

entity body: html, 파일 이 들어감



<라이브러리와 프레임워크 차이>
라이브러리는 흐름제어를 직접 해줘야하는데
프레임워크는 흐름제어를 직접 x



장고는 이미 컨트롤을 전체적으로 하고 있어서,
MVC 모델이라고 하기 힘들음



커다란 프로젝트 안에서 앱을 나눔
예를들어, www.naver.com이 하나의 프로젝트라면,
www.naver.com/webtoon 과 같이 웹툰은 앱이 된다.
즉, 하나의 프로젝트 안에 여러 앱이 존재 가능하다.



Render vs redirect
render 은 url 변경이 안댐, 부가정보 보낼 수 있음()
템플릿 폴더 안에 유저이름처럼 실행 중에 html안에서 변경하고
싶은 내용이 있어서, render로만 html에 정보를 보낼 수 있음

redirect는 url 런타임 중 변경이 됨, 






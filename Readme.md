# 구조 설명
```bash
├── src
│   ├── apps
│   │   └── [APP_NAME]
  ...
│   ├── common       # 공통 common 모음으로 build_apps.py 실행시 copy 되는 대상.
│   │   ├── __init__\ .py
│   │   ├── logger.py # log 관련 공통
│   │   ├── lmysql.py # mysql 관련 공통
│   │   ├── response.py # 응답 전문 템플릿
│   │   └── utils.py # utils
│   ├── app.py
│   └── resources.py
├── Readme.md
├── build_apps.py # Google Function deploy 를 위한 파일 정리
├── dist # Google function deploy 용 파일
├── devnev # virtualenv 폴더(python 가상환경)
├── install # requirements 전체(src/spps 하위 전체 포함) 에 대한 pip install -r 실행 for Mac
├── install.bat # install 과 동일함 for windows
├── makeDevenv # virtualenv 생성 및 activate 실행 for Mac
├── makeDevenv.bat # makeDevenv 과 동일함 for windows
├── new_app.py # 신규 app 생성 시 템플릿 생성
├── requirements.txt # 공통 적용 대상 module
├── start # flask 실행 3200 port
└── start.bat # start 과 동일함 for windows
```
# Install
### 1. Python 설치  
> version 3.8.5 [Python 3.8 download](https://www.python.org/downloads/release/python-385/)  
> 2020.12.15 일 기준 Google Functions python 3.8 이 최신 runtime 이며 상세 버전은 3.8.5로 확인
```terminal
$ pip3 --version
pip 20.1.1 from /Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/site-packages/pip (python 3.8)
```
### 2. Project initial setup
#### Install shell(Mac)
> virtualenv(가상환경 생성) 및 가상환경 활성화(activate) 후 필요 외부 module 설치
```zsh
$ pip install virtualenv
$ source ./makeDevenv
$ sh ./install
```
#### Install batch(Windows)
> virtualenv(가상환경 생성) 및 가상환경 활성화(activate) 후 필요 외부 module 설치 - windows
```bash
> pip install virtualenv
> makeDevenv.bat
> install.bat
```
> ref. 신규 외부 module 추가 경우
>> "requirements.txt" 파일에 module 명 추가 후 
>> ```zsh
>> $ sh ./install
>> ```

<br>

> ref. 가상 환경 셋업  
>> 개발 프로젝트 별 pyton version과 모듈 및 패키지 충돌을 해결하기 위해서 가상 환경 구성  
>> ```zsh
>> $ pip3 install virtualenv
>> $ virtualenv --version
>> virtualenv 20.2.2 from /Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/site-packages/virtualenv/__init__.py
>> $ virtualenv --python=python3 devenv
>> (created...)
>> $ source ./devenv/bin/activate
>> $ pip --version
>> pip 20.1.1 from /Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/site-packages/pip (python 3.8)
>> ```
>> <br>

<br>

# Start Server
> start shell 실행 하며 port 는 3200 으로 설정함.
>> Mac
>> ```zsh
>> $ sh ./start
>> ```
>> Windows
>> ```bash
>> > start.bat
>> ```

<br>

# New Function(e.g. add "youtube" Function)
> new_app.py 실행 (e.g. youtubeApp)
```bash
$ python new_app.py
Enter app name: youtubeApp

>>>>>>>>> App name is : test2
>>>>>>>>> __init__ .py created.
>>>>>>>>> main.py created.
>>>>>>>>> requirements.txt created.
>>>>>>>>>  .gcloudignore created.
```
> resources.py 파일에서 추가한 app 에 대한 route 등록(로컬 개발 테스트를 위함)
```python
from apps.youtubeApp.main import youtube
resources_apps = Blueprint('resources', __name__,)

@resources_apps.route('/youtube')
def youtube_handler():
    return youtube(request)
```

<br>

# Google Function Deploy
```bash
# 1. build_apps.py 실행
$ python build_apps.py
# dist 폴더에 베포 대상 별 폴더 생성
# > 전체 파일 copy 및 공통 requirements.txt 와 개별 requirements.txt merge 진행 됨
$ gcloud functions deploy youtube-app --entry-point youtube --runtime python38 --trigger-http --ingress-settings internal-and-gclb --region asia-northeast3
```

# SSL(For Mac)
> Finder 에서 "Install Certificates.command" 실행
>> Folder 경로 /Applications/Python 3.9 로 이동  
>> "Install Certificates.command" 실행
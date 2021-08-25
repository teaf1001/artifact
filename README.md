# 사용법
모든 파이썬 파일을 같은 경로에 놓고
python3 main.py ALL

# 코드설명

[*_parsing.py](_parsing로 끝나는 py 파일)

각 아티팩트(install, setupapi, appcache)를 추출하여 csv 파일로 저장

-------
[db_handle.py]

sqlite3 연결 모듈 호출

-------

[main.py]

아티팩트에서 추출한 정보들에서 생성한 dataframe과 생성한 sqlite3 연결 객체를 활용하여 db파일을 생성

# Assignment
# v3.8) kwargs를 사용한 데코레이터 예제.

def log_decorator(func):
    def wrapper(*args, **kwargs):
        # *변수는 위치 인수를 튜플로 저장
        # **변수는 키워드 인수를 딕셔너리에 저장
        print(f'Function Name : {func.__name__}')
        print(f'Function Arguments : {args}')
        print(f'Function Keyword Arguments : {kwargs}')
        result = func(*args, **kwargs)
        return result
    return wrapper

@log_decorator
def greet(name, greeting="안녕하세요", age=0):
    return f"{greeting}, {name}(age: {age})"if age else f"{greeting}, {name}"


print(greet("인하"))
print(greet("인상", "안녕"))
print(greet("곤잘레스", greeting="홀라"))   #키워드 인수 키=벨류 형태
print(greet("Nakamura", greeting="Gonniziwa", age=29))
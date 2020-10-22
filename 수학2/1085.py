# 현재 위치 x y 직사각형 오른쪽 위 꼭짓점 w h
# 1<=x<=w-1 1<=y<=h-1

rect = []
x, y, w, h = map(int,input().split())
rect.append(x)
rect.append(y)
rect.append(w-x)
rect.append(h-y)
print(min(rect))

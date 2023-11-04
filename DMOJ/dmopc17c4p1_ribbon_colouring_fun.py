# DMOPC '17 Contest 4 P1 - Ribbon Colouring Fun

n, q = (int(item) for item in input().split())

strokes = []

for _ in range(q):
	stroke = [int(item) for item in input().split()]
	strokes.append(stroke)
	
strokes.sort()

rightmost_position = 0

blue = 0

for stroke in strokes:
	stroke_start = stroke[0]
	stroke_end = stroke[1]
	if stroke_start <= rightmost_position:
		if stroke_end > rightmost_position:
			blue = blue + stroke_end - rightmost_position
			rightmost_position = stroke_end
	else:
		blue = blue + stroke_end - stroke_start
		rightmost_position = stroke_end

print(n - blue, blue)

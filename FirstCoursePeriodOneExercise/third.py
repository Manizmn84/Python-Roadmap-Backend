def coloring(cube: list[list[list[int]]]) -> None:
    depth = len(cube)
    rows = len(cube[0])
    cols = len(cube[0][0])
    
    for d in range(depth):
        for r in range(rows):
            for c in range(cols):
                if (
                    d == 0 or d == depth - 1 or
                    r == 0 or r == rows - 1 or
                    c == 0 or c == cols - 1
                ):
                    cube[d][r][c] = 1
                else:
                    cube[d][r][c] = 0
       

# تعریف یک ساختار سه‌بعدی
sample_cube = [
    [
        [5, 5, 5],
        [5, 5, 5],
        [5, 5, 5]
    ],
    [
        [5, 5, 5],
        [5, 5, 5],
        [5, 5, 5]
    ],
    [
        [5, 5, 5],
        [5, 5, 5],
        [5, 5, 5]
    ]
]

coloring(sample_cube)

# نمایش ساختار جدید
for i in range(len(sample_cube)):
    print(f"Layer {i + 1}:")
    for plane in sample_cube[i]:
        for element in plane:
            print(element, end=' ')
        print()
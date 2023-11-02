from fastapi import APIRouter, HTTPException, status
from pyatnashki.schemas import requestschema

router = APIRouter(
    prefix='/pyatnashki',
    tags=['pyatnashki']
)

SOLVED_STATE= [
    ['1','2'],
    ['3','x']
]

STATE_OF_THE_GAME=[]


@router.get('/')
async def get_initial_state():
    global STATE_OF_THE_GAME
    STATE_OF_THE_GAME=[
    ['1','2'],
    ['x','3']
    ]

    return STATE_OF_THE_GAME

@router.post('/')
async def change_the_game_state(
    request: requestschema.InputSchema,
):  
    global STATE_OF_THE_GAME
    # if not (request.x and request.y):
    #     print('request problem')
    #     return HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY)
    
    x_x_position = None
    y_x_position = None

    x_max = len(STATE_OF_THE_GAME[0])
    y_max = len(STATE_OF_THE_GAME)
    print(STATE_OF_THE_GAME)

    for y in range(len(STATE_OF_THE_GAME)):
        print(y)
        for x in range(len(STATE_OF_THE_GAME[y])):
            print(x)
            print('current number ',STATE_OF_THE_GAME[y][x])
            if STATE_OF_THE_GAME[y][x] == 'x':
                x_x_position = x
                y_x_position = y
                print('position of x', x_x_position, y_x_position)

    if (abs(y_x_position - request.y) > 1):
        print('error here1')
        return HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY)
    elif (abs(x_x_position - request.x) > 1):
        print('error here2')
        return HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY)

    elif abs(y_x_position - request.y) == 1 and abs(x_x_position - request.x) == 1:
        print('error here3')
        return HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY)
    
    number_to_move = STATE_OF_THE_GAME[request.y][request.x]

    STATE_OF_THE_GAME[request.y][request.x] = 'x'
    STATE_OF_THE_GAME[y_x_position][x_x_position] = number_to_move

    if STATE_OF_THE_GAME == SOLVED_STATE:
        return "YOU WON"
 
    return STATE_OF_THE_GAME
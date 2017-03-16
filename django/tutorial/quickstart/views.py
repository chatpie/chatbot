from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from tutorial.quickstart.models import *
from tutorial.quickstart.serializers import *
import json

@api_view(['GET'])
def keyboard(request):
    """
    이용자가 최초로 채팅방에 들어올 때 기본으로 키보드 영역에 표시될
    자동응답 명령어의 목록을 호출하는 API입니다.
    """
    if request.method == 'GET':
        keyboard = Keyboard.create()
        serializer = KeyboardSerializer(keyboard)
        return Response(serializer.data)

@api_view(['POST'])
def message(request):
    """
    사용자가 선택한 명령어를 파트너사 서버로 전달하는 API입니다.
    자동응답 명령어에 대한 답변은 응답 메시지(Message)와
    응답 메시지에 따른 키보드 영역의 답변 방식(Keyboard)의 조합으로 이루어집니다.
    답변 방식은 주관식(text)과 객관식(buttons) 중 선택할 수 있습니다.
    """
    user_text = request.data['content']

    if request.method == 'POST':
        message = Message.create(user_text)
        messageResponse = MessageResponse.create(message)
        serializer = MessageResponseSerializer(messageResponse)
        return Response(serializer.data)

@api_view(['POST','DELETE'])
def friend(request):
    """
    특정 카카오톡 이용자가 플러스친구/옐로아이디를 친구로 추가하거나
    차단하는 경우 해당 정보를 파트너사 서버로 전달하는 API입니다.
    """
    return Response(status=status.HTTP_200_OK)

@api_view(['DELETE'])
def chat_room(request):
    """
    사용자가 채팅방 나가기를 해서 채팅방을 목록에서 삭제했을 경우
    해당 정보를 파트너사 서버로 전달하는 API입니다.
    """
    return Response(status=status.HTTP_200_OK)

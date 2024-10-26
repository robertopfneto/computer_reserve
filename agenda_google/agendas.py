import datetime
import os
import pickle

from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build

from authenticate import authenticate_google_calendar

def list_gpus_available(service, calendar_id, date=None):
    if date is None:
        date = datetime.date.today()
    
    start_of_day = datetime.datetime.combine(date, datetime.time.min).isoformat() + 'Z'
    end_of_day = datetime.datetime.combine(date, datetime.time.max).isoformat() + 'Z'
    
    events_result = service.events().list(calendarId=calendar_id, timeMin=start_of_day,
                                          timeMax=end_of_day, singleEvents=True,
                                          orderBy='startTime').execute()
    events = events_result.get('items', [])
    
    if not events:
        print('Nenhuma reserva de GPU encontrada para o dia.')
        return []
    
    reserved_gpus = [event['summary'] for event in events]
    print(f'GPUs reservadas: {reserved_gpus}')
    
    all_gpus = [f'GPU {i+1}' for i in range(8)]  # Defina no Range a quantidade de GPUS disponiveis
    available_gpus = [gpu for gpu in all_gpus if gpu not in reserved_gpus]
    
    print(f'GPUs disponíveis: {available_gpus}')
    return available_gpus

def reserve_gpu(service, gpu_name, start_time, end_time, calendar_id):
    """Reserva uma GPU disponível"""
    event = {
        'summary': gpu_name,
        'start': {
            'dateTime': start_time,
            'timeZone': 'America/Sao_Paulo',
        },
        'end': {
            'dateTime': end_time,
            'timeZone': 'America/Sao_Paulo',
        }
    }
    
    event = service.events().insert(calendarId=calendar_id, body=event).execute()
    print(f'Reserva confirmada para {gpu_name} das {start_time} às {end_time}')

if __name__ == '__main__':
    # Autentica e cria o serviço da API
    service = authenticate_google_calendar()
    
    # Define o ID da agenda "RESERVA DE GPUs DO INOVISAO"
    calendar_id = 'INSIRA_O_ID_DA_AGENDA_AQUI'

    # Exibe GPUs disponíveis para o dia atual
    available_gpus = list_gpus_available(service, calendar_id)

    if available_gpus:
        gpu_to_reserve = available_gpus[0]
        start_time = datetime.datetime.now().replace(hour=10, minute=0).isoformat() + 'Z'
        end_time = datetime.datetime.now().replace(hour=12, minute=0).isoformat() + 'Z'
        
        reserve_gpu(service, gpu_to_reserve, start_time, end_time, calendar_id)

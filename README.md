//PT-BR

# Reserva de GPU no Google Agenda

Este projeto permite gerenciar a reserva de GPUs disponíveis em um Google Agenda. Ele permite listar quais GPUs estão disponíveis em um determinado dia e criar reservas de acordo com as preferências do usuário.

## Recursos

- **Listar GPUs disponíveis:** Exibe GPUs que não estão reservadas no dia atual.
- **Reservar GPU:** Reserva uma GPU para um intervalo de tempo específico no Google Agenda.

## Pré-requisitos

Este projeto requer uma conta do Google e permissões para acessar a API do Google Agenda. Além disso, o arquivo `credentials.json`, obtido do Google Cloud Console, é necessário para autenticação da API.

### Dependências

As seguintes bibliotecas Python são necessárias:

```bash
pip install google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client
```

## Arquivos

- **agendas.py:** Código principal que lista e reserva GPUs no Google Agenda.
- **authenticate_google_calendar:** Função de autenticação que configura o serviço de API.
- **token.pickle:** Arquivo gerado automaticamente que armazena o token de autenticação.

## Configuração

1. **Configurar a API do Google Agenda:**
- Acesse o [Google Cloud Console](https://console.cloud.google.com/) e crie um projeto.
- Habilite a API do Google Agenda para o projeto.
- Baixe o arquivo `credentials.json` e salve-o na mesma pasta do código.

2. **Autenticação:**
- Execute o código pela primeira vez para autenticar. Um arquivo `token.pickle` será gerado para armazenar o token para autenticações futuras.

## Uso

### Listar GPUs disponíveis

Para listar as GPUs disponíveis no dia atual, execute `agendas.py`. Ele exibirá as reservas existentes e listará as GPUs disponíveis.

### Reservar GPU

O script inclui uma reserva de GPU de exemplo:
- Ajuste o horário de início (`start_time`) para o horário atual do computador e especifique o horário de término desejado (`end_time`) no formato ISO 8601.
- Certifique-se de inserir o **ID do calendário** em `calendar_id` onde as reservas serão feitas.

```python
# Exemplo de uso para reserva
service = authenticate_google_calendar()
calendar_id = 'INSERT_CALENDAR_ID_HERE'
list_gpus_available(service, calendar_id)
```

Para agendar uma GPU disponível:

```python
reserve_gpu(service, gpu_to_reserve, start_time, end_time, calendar_id)
```


//EN
# GPU Reservation on Google Calendar

This project enables managing the reservation of available GPUs on a Google Calendar. It allows listing which GPUs are available on a given day and creating reservations according to user preferences.

## Features

- **List Available GPUs:** Displays GPUs that are not reserved on the current day.
- **Reserve GPU:** Reserves a GPU for a specific time interval on the Google Calendar.

## Prerequisites

This project requires a Google account and permissions to access the Google Calendar API. Additionally, the `credentials.json` file, obtained from the Google Cloud Console, is necessary for API authentication.

### Dependencies

The following Python libraries are required:

```bash
pip install google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client
```

## Files

- **agendas.py:** Main code that lists and reserves GPUs on Google Calendar.
- **authenticate_google_calendar:** Authentication function that sets up the API service.
- **token.pickle:** Automatically generated file that stores the authentication token.

## Setup

1. **Set up Google Calendar API:**
   - Go to the [Google Cloud Console](https://console.cloud.google.com/) and create a project.
   - Enable the Google Calendar API for the project.
   - Download the `credentials.json` file and save it in the same folder as the code.

2. **Authentication:**
   - Run the code for the first time to authenticate. A `token.pickle` file will be generated to store the token for future authentications.

## Usage

### List Available GPUs

To list the GPUs available on the current day, run `agendas.py`. It will display existing reservations and list the available GPUs.

### Reserve GPU

The script includes a sample GPU reservation:
- Adjust the start time (`start_time`) to the computer’s current time and specify the desired end time (`end_time`) in ISO 8601 format.
- Make sure to insert the **calendar ID** in `calendar_id` where reservations will be made.

```python
# Example usage for reservation
service = authenticate_google_calendar()
calendar_id = 'INSERT_CALENDAR_ID_HERE'
list_gpus_available(service, calendar_id)
```

To schedule an available GPU:

```python
reserve_gpu(service, gpu_to_reserve, start_time, end_time, calendar_id)
```


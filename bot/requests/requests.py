import aiohttp
import asyncio


class Requests:
    def __init__(self):
        self.url = "http://127.0.0.1:8000/"

    async def check_student_or_add(self, chat_id):
        async with aiohttp.ClientSession() as session:
            async with session.get(self.url + f'students/{chat_id}/') as response:
                if response.status == 200:
                    print(f"Student with chat_id {chat_id} exists.")
                    return {"status": "exists", "chat_id": chat_id}
                elif response.status == 404:
                    print(f"Student with chat_id {chat_id} not found. Adding new student.")
                    student_data = {
                        "student_chat_id": chat_id
                    }

                    async with session.post(self.url + 'students/', json=student_data) as add_response:
                        if add_response.status == 201:
                            print(f"New student with chat_id {chat_id} added.")
                            return {"status": "added", "chat_id": chat_id}
                        else:
                            print(f"Failed to add student. Status code: {add_response.status}")
                            return {"status": "error", "message": "Failed to add student."}
                else:
                    print(f"Unexpected response status: {response.status}")
                    return {"status": "error", "message": "Unexpected response status"}

    async def add_student_language(self, chat_id, language):
        student_data = {
            "language": language
        }
        async with aiohttp.ClientSession() as session:
            async with session.patch(self.url + f'students/{chat_id}/', json=student_data) as response:
                if response.status == 200:
                    print(f"Student with chat_id {chat_id} language updated to {language}.")
                    return {"status": "updated", "chat_id": chat_id, "language": language}
                elif response.status == 404:
                    print(f"Student with chat_id {chat_id} not found.")
                    return {"status": "error", "message": "Student not found."}
                else:
                    print(f"Failed to update student. Status code: {response.status}")
                    return {"status": "error", "message": "Failed to update student."}

    async def get_user_language(self, chat_id):
        async with aiohttp.ClientSession() as session:
            async with session.get(self.url + f'students/{chat_id}/') as response:
                if response.status == 200:
                    student_data = await response.json()
                    language = student_data.get("language")
                    if language:
                        print(f"Student's language: {language}")
                        return {"status": "success", "language": language}
                    else:
                        print(f"Language not found for chat_id {chat_id}")
                        return {"status": "error", "message": "Language not found"}
                else:
                    print(f"Failed to retrieve student with chat_id {chat_id}. Status code: {response.status}")
                    return {"status": "error", "message": "Failed to retrieve student data"}

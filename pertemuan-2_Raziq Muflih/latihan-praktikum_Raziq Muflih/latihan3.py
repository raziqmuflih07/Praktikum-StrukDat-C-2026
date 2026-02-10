tim_frontend= {"HTML", "css","JavaScript","React"}
tim_backend= {"Python","JavaScript","SQL","NodeJs"}

irisan = tim_frontend.intersection(tim_backend)
backend_only = tim_backend.difference(tim_frontend)
union_skill = tim_frontend | tim_backend

print(f"Irisan: {irisan}")
print(f"Skill Tim Backend: {backend_only}")
print(f"Skill Gabungan: {union_skill}")

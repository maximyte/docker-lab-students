import redis

# ВПИШИТЕ имя контейнера Redis (задание 8):
r = redis.Redis(host="redis-server", port=6379)
r.set("message", "Hello from Python")
print("Message set in Redis")

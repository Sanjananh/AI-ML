try:
    file=open("file.txt", "r")
    print(file.read())
except Exception as e:
    print("An error occurred:", e)
    print(f"Error:{e}")
finally:
    file.close()
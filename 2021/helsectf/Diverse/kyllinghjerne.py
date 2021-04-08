from keras.models import load_model


model = load_model('kyllinghjerne/chicken.h5')
#print(model.summary())

with open("kyllinghjerne/input.txt") as f:
    inputs = [[list([(ch=='X')-0.5] for ch in f.readline()[:28])
              for b in range(28)]
              for i in range(10)]

pred = model.predict(inputs)
#print(asd)

print("IN:", len(inputs), len(inputs[0]), len(inputs[0][0]))
print("OUT:", len(pred), len(pred[0]), len(pred[0][0]))

with open("kyllinghjerne/egg.txt", "w+") as f:
    for char in pred:
        for line in char:
            line = ["X" if ch>0.5 else " " for ch in line]
            print(line)
            f.write("".join(line))

#print(inputs[5][5])
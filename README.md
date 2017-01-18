# Traffic Light Recognition Network

This model was created for the [nexar](https://www.getnexar.com/) challenge 1.
It reached 93.6% accuracy on the challenge test data.

This work is based on the [squeezeNet](https://arxiv.org/abs/1602.07360)
model and it's [kera's implementation](https://github.com/DT42/squeezenet_demo).

# Using
in order to use the model to classify image to 3 classes:

 - no traffic light
 - red light
 - green light

just edit the variable `TEST_FOLDER` in pred.py file.
then:
```
python pred.py
```

it will create csv file: `results.csv`


## Auther
[Guy Hadash](https://www.linkedin.com/in/guy-hadash-b86a8031)
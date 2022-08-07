# Neural Network From Scratch For a simple Path finding game.

## Architecture

### Network

It is a simple architecture of 4 layers of neurons.

- First Layer has 10 input parameters.

    1. Distance from top wall.

    2. Distance from top-right wall.

    3. Distance from right wall.

    4. Distance from bottom-right wall.

    5. Distance from bottom wall.

    6. Distance from bottom-left wall.

    7. Distance from left wall.

    8. Distance from top-left wall.

    9. Distance from the destination.

    10. Angle towards the distance.

- Second Layer is a 10 node hidden layer.

- Third layer is also a 10 layer hidden layer.

- The final output layer consists fo 4 nodes. Each signifying the urge to move in one direction.

    1. Move Top

    2. Move Right

    3. Move Bttom

    4. Move Left

Each layer is connected to all the nodes from previous layer with some weight and biases.

### Activation Function

This model uses Sigmoid activation function for all layers.

![Sigmoid Function](https://github.com/AnjaanKhadka/Single-purpose-Neural-Network-From-Scratch/blob/master/Result_images/sigmoid.png)

### Cost Function / Points system

Cost of the bot is measured by calculating distance from next checkpoint. This model tries to maximize the points. after each checkpoint it adds 10000 points.

### Backpropagation and learning Process

This system is simplest form of neural network. Thus I have not implemented any backpropagation for learning. Thus it relies on ramdom luck for minimizing cost.

Every weights and biases changes on each generation. Each generation generates 500 bots. among last 500 generation, 100 best performing bots weight and biases are tweeked by small value at random thus random learning. There is an small chance of some bots being offspring of one of lower 400 bots.

## Requirements

Requirements of this project are listed in [requirements.txt](https://github.com/AnjaanKhadka/Single-purpose-Neural-Network-From-Scratch/blob/master/requirements.txt). To install all requirements execute following code.

    pip install -r requirements.txt

## Training

To Train, clone this repo and execute following commmands

    python main.py

## Results

I have trained for about 3 hours to 200 generations. But best run was from generation 139. because it is a random chance, learning peaked after 139 generations. Till this generation I could train to pass 1st checkpoint. This model could not find weights for passing 2nd checkpoint whatsoever.

Result of Start of Training in generation2

![1st Result](https://github.com/AnjaanKhadka/Single-purpose-Neural-Network-From-Scratch/blob/master/Result_images/result1.png)

Result of crossing 1st big obstacle generation 52

![2nd Result](https://github.com/AnjaanKhadka/Single-purpose-Neural-Network-From-Scratch/blob/master/Result_images/result2.png)

Result of crossing 1st Checkpoint in generation 139

![3rd Result](https://github.com/AnjaanKhadka/Single-purpose-Neural-Network-From-Scratch/blob/master/Result_images/result3.png)


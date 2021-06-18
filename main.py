from flask import Flask
import torch

app = Flask(__name__)


@app.route('/')
def index():
    grad_x = torch_example()
    return grad_x


def torch_example():
    # Create tensors.
    x = torch.tensor(1., requires_grad=True)
    w = torch.tensor(2., requires_grad=True)
    b = torch.tensor(3., requires_grad=True)

    # Build a computational graph.
    y = w * x + b  # y = 2 * x + 3

    # Compute gradients.
    y.backward()

    # gradients
    a = x.grad
    return a


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port="5001")

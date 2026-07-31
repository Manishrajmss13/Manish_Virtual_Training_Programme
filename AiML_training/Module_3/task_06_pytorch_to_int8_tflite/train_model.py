
import os
import numpy as np

import torch
import torch.nn as nn
import torch.optim as optim

from torchvision import datasets, transforms
from torch.utils.data import DataLoader

from model_definition import SimpleCNN


def main():

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    print("Using device:", device)

    transform = transforms.Compose([
        transforms.ToTensor()
    ])

    train_data = datasets.MNIST(
        "./data",
        train=True,
        download=True,
        transform=transform
    )

    test_data = datasets.MNIST(
        "./data",
        train=False,
        download=True,
        transform=transform
    )

    train_loader = DataLoader(
        train_data,
        batch_size=64,
        shuffle=True
    )

    test_loader = DataLoader(
        test_data,
        batch_size=64,
        shuffle=False
    )

    model = SimpleCNN().to(device)

    criterion = nn.CrossEntropyLoss()

    optimizer = optim.Adam(
        model.parameters(),
        lr=0.001
    )

    epochs = 5

    for epoch in range(epochs):

        model.train()

        running_loss = 0

        for images, labels in train_loader:

            images = images.to(device)
            labels = labels.to(device)

            optimizer.zero_grad()

            outputs = model(images)

            loss = criterion(outputs, labels)

            loss.backward()

            optimizer.step()

            running_loss += loss.item()

        print(f"Epoch {epoch+1}/{epochs} Loss = {running_loss/len(train_loader):.4f}")

    model.eval()

    correct = 0
    total = 0

    with torch.no_grad():

        for images, labels in test_loader:

            images = images.to(device)
            labels = labels.to(device)

            outputs = model(images)

            _, predicted = torch.max(outputs, 1)

            total += labels.size(0)

            correct += (predicted == labels).sum().item()

    accuracy = 100 * correct / total

    print(f"Test Accuracy = {accuracy:.2f}%")

    torch.save(model.state_dict(), "model.pth")

    print("Saved model.pth")

    os.makedirs("calib", exist_ok=True)

    for i in range(50):

        sample, _ = test_data[i]

        sample = np.expand_dims(sample.numpy(), axis=0)

        np.save(f"calib/{i}.npy", sample)

    print("Calibration data created.")


if __name__ == "__main__":
    main()

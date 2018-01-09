# coding=utf-8
"""
@version: 2017/12/27 027
@author: Suen
@contact: sunzh95@hotmail.com
@file: face_recognition_ex
@time: 14:10
@note:  ??
"""

from sklearn import datasets
from sklearn.model_selection import GridSearchCV, train_test_split
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.decomposition import PCA
from sklearn.svm import SVC
import matplotlib.pyplot as plt


def plot_gallery(images, titles, h, w, n_rows=3, n_cols=4):
    plt.figure(figsize=(1.8 * n_cols, 2.4 * n_rows))
    plt.subplots_adjust(bottom=0, left=.01, right=.9, top=.9, hspace=.35)
    for i in range(n_rows * n_cols):
        plt.subplot(n_rows, n_cols, i + 1)
        plt.imshow(images[i].reshape((h, w)), cmap=plt.cm.gray)
        plt.title(titles[i], size=12)
        plt.xticks(())
        plt.yticks(())
    plt.show()


def title(y_pred, y_test, target_names, i):
    pred_name = target_names[y_pred[i]].rsplit(' ', 1)[-1]
    true_name = target_names[y_test[i]].rsplit(' ', 1)[-1]
    return 'true:    %s\npredict: %s' % (true_name, pred_name)


if __name__ == '__main__':
    lfw_people = datasets.fetch_lfw_people(min_faces_per_person=70, resize=0.4)
    n_samples, h, w = lfw_people.images.shape

    x = lfw_people.data  # features values
    n_features = x.shape[1]  # features number

    y = lfw_people.target  # target values
    target_names = lfw_people.target_names
    n_labels = target_names.size

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25)

    n_components = 150  # components to be kept
    pca = PCA(n_components, svd_solver='randomized', whiten=True).fit(x_train)

    eigenfaces = pca.components_.reshape(n_components, h, w)

    x_train_pca = pca.transform(x_train)
    x_test_pca = pca.transform(x_test)

    param_grid = {'C': [1e3, 5e3, 1e4, 5e4, 1e5], 'gamma': [0.0001, 0.0005, 0.001, 0.005, 0.01, 0.1]}
    clf = GridSearchCV(SVC(kernel='rbf'), param_grid)
    clf.fit(x_train_pca, y_train)
    print(clf.best_estimator_)

    y_predict = clf.predict(x_test_pca)

    print(classification_report(y_test, y_predict, target_names=target_names))
    print(confusion_matrix(y_test, y_predict, labels=range(n_labels)))

    titles = [title(y_predict, y_test, target_names, i) for i in range(y_predict.size)]

    plot_gallery(x_test, titles, h, w)

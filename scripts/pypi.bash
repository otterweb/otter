
python3.7 setup.py sdist bdist_wheel

if [ $? -ne 0 ]; then exit 1; fi


#python3.7 -m twine upload --verbose --repository-url https://test.pypi.org/legacy/ dist/*

python3.7 -m twine upload -r $1 dist/*





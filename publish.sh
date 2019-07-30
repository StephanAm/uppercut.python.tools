# remove old artefacts
#rm -r ./dist
# build new distribution
python3 setup.py sdist bdist_wheel step
# upload package
#python3 -m twine upload dist/*

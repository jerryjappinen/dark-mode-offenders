# Source code

This `src/` folder is the source code needed to build the Readme you see on the root folder of this project.

All dark mode offender data is in `apps.csv` and `updates.csv`.

Run `build.py` to compose the final readme and JSON. This will be run by GitHub actions upon push.

### Development

```
# Activate local Python virtual environment
source .venv/bin/activate

# Run scripts
python3 src/main.py build
python3 src/main.py print
python3 src/main.py stats
python3 src/main.py test
```

```
# Keep tests running
# Needs node (e.g. nvm use 22)
npx nodemon --exec python3 src/main.py test
```

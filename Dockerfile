FROM python:3.10-slim

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PIP_DEFAULT_TIMEOUT=120 \
    LC_ALL=C.UTF-8 \
    LANG=C.UTF-8

# we probably need build tools?
RUN apt-get update \
    && apt-get install --yes --no-install-recommends \
    gcc \
    g++ \
    build-essential \
    python3-dev

WORKDIR /app
COPY requirements.txt requirements.txt

RUN xargs -a packages.txt apt-get install --yes

RUN pip install --no-cache-dir --upgrade -r requirements.txt

## Install js libraries
# ENV NODE_VERSION=16.13.0
# RUN apt install -y curl
# RUN curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.0/install.sh | bash
# ENV NVM_DIR=/root/.nvm
# RUN . "$NVM_DIR/nvm.sh" && nvm install ${NODE_VERSION}
# RUN . "$NVM_DIR/nvm.sh" && nvm use v${NODE_VERSION}
# RUN . "$NVM_DIR/nvm.sh" && nvm alias default v${NODE_VERSION}
# ENV PATH="/root/.nvm/versions/node/v${NODE_VERSION}/bin/:${PATH}"
# RUN node --version
# RUN npm --version
# RUN npm install mermaid

EXPOSE 8501

COPY . .

CMD ["streamlit", "run", "streamlit_app.py"]

# docker build --progress=plain --tag pydub:latest .
# docker run -ti -p 8501:8501 --rm pydub:latest /bin/bash
# docker run -ti -p 8501:8501 --rm pydub:latest
# docker run -ti -p 8501:8501 -v ${pwd}:/app --rm pydub:latest
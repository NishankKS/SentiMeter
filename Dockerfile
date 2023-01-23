FROM nvcr.io/nvidia/pytorch:22.07-py3

COPY ./Makefile /workspace/Makefile
COPY ./requirements.txt /workspace/requirements.txt
RUN make install

COPY ./app /workspace
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
EXPOSE 8000
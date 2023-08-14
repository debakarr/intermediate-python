topics = [
    "[Basic Overview](./01_python_basic_overview.ipynb)",
    "[Memory Management in Python](./02_memory_management_in_python.ipynb)",
    "[Function parameters and arguments](./03_function_parameters_and_arguments.ipynb)",
    "[Namespace, Scope and Closure](./04_namespaces_scopes_and_closures.ipynb)",
    "[Other functions concepts](./05_other_functions_concepts.ipynb)",
    "[Sequence, Iterator and Generator](./06_sequence_iterators_and_generators.ipynb)",
    "[Content Manager](./07_context_managers.ipynb)",
    "[Building command line interface](./08_argparse/09_argparse.ipynb)",
    "[Testing](./09_unittest.ipynb)",
    "[Multithreading and Multiprocessing](./10_concurrency.ipynb)",
    "[Virtual Environments](./11_virtual_environment.ipynb)",
    "[Packaging](./12_packaging.ipynb)",
    "[Debugging in Python](./13_debugging.ipynb)",
    "[Command line tools in Python Standard library](./14_python_builtin_cli.ipynb)",
    "[Python Toolkit for Production](./15_python_toolkit.ipynb)",
]

for i, _ in enumerate(topics):
    prev_topic = "[]()" if i == 0 else topics[i - 1]
    next_topic = "[]()" if i == len(topics) - 1 else topics[i + 1]
    print(rf"\[<< {prev_topic} | [Index](./00_index.ipynb) | {next_topic} >>\]")

import heavy.compute_one_block.wrapped_models.block as block
import heavy.compute_one_block.wrapped_models.progress as progress
import heavy.compute_one_block.wrapped_models.range as ranged
import heavy.compute_one_block.wrapped_models.resulting as resulting


def main(mode, inputs, outputs, ranges, progressbar, results):
    """Entrypoint of script that's executing by `specific-eval-exec` block algorithm.
    :type mode: str
    :type inputs: list[block.Input]
    :type outputs: list[block.Output]
    :type ranges: ranged.Ranges
    :type progressbar: progress.ComputeProgress
    :type results: resulting.Results
    """
    pass

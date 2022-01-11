from .entities.model import Model
from .repositories.repository import Repository as ModelRepository


def api_request_logs():
    """Returns repository of `ApiRequestLog` model.
    :rtype: AsyncOperationRepository
    """
    pass


def async_operations():
    """Returns repository of `AsyncOperation` model.
    :rtype: AsyncOperationRepository
    """
    pass


def blocks():
    """Returns repository of `Block` model.
    :rtype: BlockRepository
    """
    pass


def cache_models(mask, *args):
    """Returns repository of `CacheModel` model.
    
    Available `args`:
        – %index%: any
    :type mask: str
    :rtype: CacheModelRepository
    """
    pass


def credentials():
    """Returns repository of `Credential` model.
    :rtype: CredentialRepository
    """
    pass


def eval_exec():
    """Returns repository of `EvalExec` model.
    :rtype: EvalExecRepository
    """
    pass


def exported_files():
    """Returns repository of `ExportedFile` model.
    :rtype: ExportedFileRepository
    """
    pass


def imported_files():
    """Returns repository of `ImportedFile` model.
    :rtype: ImportedFileRepository
    """
    pass


def intermediate_files():
    """Returns repository of `IntermediateFile` model.
    :rtype: IntermediateFileRepository
    """
    pass


def organizations():
    """Returns repository of `Organization` model.
    :rtype: OrganizationRepository
    """
    pass


def progress_logs():
    """Returns repository of `ProgressLog` model.
    :rtype: ProgressLogRepository
    """
    pass


def reports():
    """Returns repository of `Report` model.
    :rtype: ReportRepository
    """
    pass


def services():
    """Returns repository of `Service` model.
    :rtype: ServiceRepository
    """
    pass


def users():
    """Returns repository of `User` model.
    :rtype: UserRepository
    """
    pass

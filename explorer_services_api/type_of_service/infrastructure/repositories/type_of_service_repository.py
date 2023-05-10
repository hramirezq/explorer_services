from django.db import connection

from explorer_services_api.type_of_service.domain.utils.cursor_to_dictionary import CursorToDictionary


class TypeOfServiceRepository:

    @staticmethod
    def get_by_id(type_of_service_id):
        """
            This method is used to obtain a service type and its nested objects,
            such as packages and deliverables.

            Args:
                type_of_service_id: Service type identifier.

            Raises:
                TypeOfService.DoesNotExist: When the object does not exist, a none is returned.

        """

        query = """
        SELECT * FROM type_of_services t
        INNER JOIN packages  p  on t.Id = p.type_of_service_id_id  
        INNER JOIN deliverables d ON p.id = d."package_Id_id" 
        WHERE t.id = {id}
        """.format(id=type_of_service_id)
        with connection.cursor() as cursor:
            cursor.execute(query)
            result_query = CursorToDictionary().run(cursor)

        return result_query

    @staticmethod
    def get_all():
        """
        This method is used to obtain all types of services
        """
        query = """
                SELECT * FROM type_of_services t
                INNER JOIN packages  p  on t.Id = p.type_of_service_id_id  
                INNER JOIN deliverables d ON p.id = d."package_Id_id" 
                """
        with connection.cursor() as cursor:
            cursor.execute(query)
            result_query = CursorToDictionary().run(cursor)

        return result_query
